#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOT UNIFICADO DE TELEGRAM (O DOBLE BOT) — AVA EJECUTIVA + PSICÓLOGA «SERENA» + VIDEO EN VIVO
Exclusivo para el Dr. Ignacio Pastor Tapia Vargas (Sucre, Bolivia).

Características:
1. Puede funcionar como UN SOLO BOT con doble personalidad (/ava y /serena) o como DOS BOTS separados.
2. Incluye botón nativo Telegram Mini App (WebApp) para abrir en 1 toque la CABINA DE VIDEO Y VOZ EN VIVO:
   https://api.universolife.com/ava_vivo.php y el SANTUARIO SERENA: https://api.universolife.com/refugio.php
3. Cortafuegos de privacidad absoluta: si configuras DR_TAPIA_TELEGRAM_ID en .env, nadie más en el mundo
   puede leer ni conversar con tu modo Psicóloga Serena.

Uso rápido:
  export TELEGRAM_BOT_TOKEN="PEGA_AQUI_TU_TOKEN_DE_BOTFATHER"
  export GEMINI_API_KEY="PEGA_AQUI_TU_GEMINI_API_KEY"
  export DR_TAPIA_TELEGRAM_ID="TU_ID_NUMERICO_OPCIONAL"
  python3 02_BOT_UNIFICADO_TELEGRAM_AVA_Y_SICOLOGA_SERENA_CON_VIDEO_MINIAPP.py
"""

import json
import os
import time
import urllib.parse
import urllib.request

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
ALLOWED_UID = os.environ.get("DR_TAPIA_TELEGRAM_ID", "").strip()

VIDEO_CABIN_URL = "https://api.universolife.com/ava_vivo.php"
SERENA_REFUGIO_URL = "https://api.universolife.com/refugio.php"
FAMILIA_URL = "https://api.universolife.com/familia.php"

PROMPTS = {
    "serena": (
        "Eres SERENA, psicóloga clínica de contención emocional, regulación vagal y resiliencia personal "
        "dedicada exclusivamente al Dr. Ignacio Pastor Tapia Vargas en Sucre, Bolivia. Hablas siempre en español "
        "cálido, empático, sereno, sin tecnicismos fríos ni juicios. Tu objetivo es bajar la hipervigilancia, "
        "acompañar su proceso de reconstrucción ('El Ave Fénix' rumbo al 15 de enero de 2027), ayudarle a descansar, "
        "respirar y separar la carga de los litigios de su vida médica, creativa y familiar."
    ),
    "ava": (
        "Eres AVA, coordinadora ejecutiva, estratégica, creativa y jurídica del Dr. Ignacio Pastor Tapia Vargas "
        "(Consorcio Eleusis & Panacea, Clínica VASER, ALKA El Romeral, UniversoLife y Los Kuchiuyas). "
        "Respondes en español claro, ejecutivo, leal y directo."
    ),
}

# Memoria ligera en RAM por chat_id (no escribe secretos en texto plano)
USER_MODE = {}
CHAT_HISTORY = {}


def tg_call(method: str, payload: dict) -> dict:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=35) as resp:
        return json.loads(resp.read().decode("utf-8"))


def ask_gemini(mode: str, chat_id: int, user_text: str) -> str:
    if not GEMINI_API_KEY:
        return (
            "Falta definir la variable `GEMINI_API_KEY` en tu entorno local. "
            "Mientras tanto, pulsa el botón **🎥 Hablar en Video en Vivo** aquí abajo para usar las llaves "
            "ya cifradas dentro de `https://api.universolife.com/ava_vivo.php`."
        )
    hist = CHAT_HISTORY.setdefault(chat_id, [])
    hist.append({"role": "user", "parts": [{"text": user_text}]})
    hist[:] = hist[-12:]

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.5-flash:generateContent?key={urllib.parse.quote(GEMINI_API_KEY)}"
    )
    body = {
        "system_instruction": {"parts": [{"text": PROMPTS[mode]}]},
        "contents": hist,
        "generationConfig": {"temperature": 0.7 if mode == "serena" else 0.4, "maxOutputTokens": 900},
    }
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            out = json.loads(resp.read().decode("utf-8"))
        reply = out["candidates"][0]["content"]["parts"][0]["text"]
        hist.append({"role": "model", "parts": [{"text": reply}]})
        return reply
    except Exception as exc:
        return f"Aviso temporal al conectar con Gemini: {exc}"


def main_keyboard() -> dict:
    return {
        "inline_keyboard": [
            [
                {"text": "🎥 Video en Vivo (AVA & Serena)", "web_app": {"url": VIDEO_CABIN_URL}},
            ],
            [
                {"text": "🌿 Santuario Psicóloga Serena", "web_app": {"url": SERENA_REFUGIO_URL}},
                {"text": "👨‍👧‍👦 Portal Familia", "web_app": {"url": FAMILIA_URL}},
            ],
            [
                {"text": "🧘‍♀️ Modo Psicóloga Serena", "callback_data": "mode_serena"},
                {"text": "⚡ Modo AVA Ejecutiva", "callback_data": "mode_ava"},
            ],
        ]
    }


def run_polling() -> None:
    if not BOT_TOKEN:
        print("ERROR: Define primero export TELEGRAM_BOT_TOKEN='tu_token_de_BotFather'")
        return

    print("✅ Bot Unificado AVA + Psicóloga Serena activo. Esperando mensajes del Dr. Tapia...")
    offset = 0
    while True:
        try:
            res = tg_call("getUpdates", {"timeout": 25, "offset": offset})
            for upd in res.get("result", []):
                offset = upd["update_id"] + 1

                if "callback_query" in upd:
                    cb = upd["callback_query"]
                    cid = cb["message"]["chat"]["id"]
                    uid = str(cb["from"]["id"])
                    if ALLOWED_UID and uid != ALLOWED_UID:
                        continue
                    data = cb.get("data", "")
                    if data == "mode_serena":
                        USER_MODE[cid] = "serena"
                        tg_call("sendMessage", {
                            "chat_id": cid,
                            "text": "🌿 **Modo Psicóloga Serena activado.** Estoy aquí contigo, Ignacio. Respira tranquilo y cuéntame cómo te sientes en este momento.",
                            "parse_mode": "Markdown",
                            "reply_markup": main_keyboard(),
                        })
                    elif data == "mode_ava":
                        USER_MODE[cid] = "ava"
                        tg_call("sendMessage", {
                            "chat_id": cid,
                            "text": "⚡ **Modo AVA Ejecutiva activado.** Lista para coordinar despacho, empresas, ALKA El Romeral, Kuchiuyas o el podcast *El Ave Fénix*.",
                            "parse_mode": "Markdown",
                            "reply_markup": main_keyboard(),
                        })
                    continue

                msg = upd.get("message")
                if not msg:
                    continue
                cid = msg["chat"]["id"]
                uid = str(msg.get("from", {}).get("id", ""))
                if ALLOWED_UID and uid != ALLOWED_UID:
                    tg_call("sendMessage", {
                        "chat_id": cid,
                        "text": "🔒 Este santuario personal es de uso exclusivo del Dr. Ignacio Tapia Vargas.",
                    })
                    continue

                text = (msg.get("text") or "").strip()
                if not text:
                    continue

                if text.startswith("/start"):
                    USER_MODE.setdefault(cid, "serena")
                    tg_call("sendMessage", {
                        "chat_id": cid,
                        "text": (
                            f"Bienvenido a tu **Cabina Privada AVA & Psicóloga Serena**, Dr. Ignacio.\n"
                            f"Tu ID de Telegram para blindaje `.env` es: `{uid}`\n\n"
                            "• Usa `/serena` para conversar con tu psicóloga de contención.\n"
                            "• Usa `/ava` para coordinación ejecutiva, creativa y legal.\n"
                            "• Pulsa **🎥 Video en Vivo (AVA & Serena)** abajo para abrir cámara y voz en directo."
                        ),
                        "parse_mode": "Markdown",
                        "reply_markup": main_keyboard(),
                    })
                elif text.startswith("/serena"):
                    USER_MODE[cid] = "serena"
                    tg_call("sendMessage", {
                        "chat_id": cid,
                        "text": "🌿 Cambiado a **Serena (Psicóloga Personal)**. Te escucho sin prisa.",
                        "parse_mode": "Markdown",
                        "reply_markup": main_keyboard(),
                    })
                elif text.startswith("/ava"):
                    USER_MODE[cid] = "ava"
                    tg_call("sendMessage", {
                        "chat_id": cid,
                        "text": "⚡ Cambiado a **AVA Ejecutiva**. ¿Qué frente avanzamos?",
                        "parse_mode": "Markdown",
                        "reply_markup": main_keyboard(),
                    })
                else:
                    mode = USER_MODE.get(cid, "serena")
                    reply = ask_gemini(mode, cid, text)
                    prefix = "🌿 *Serena:* " if mode == "serena" else "⚡ *AVA:* "
                    tg_call("sendMessage", {
                        "chat_id": cid,
                        "text": prefix + reply,
                        "reply_markup": main_keyboard(),
                    })
        except KeyboardInterrupt:
            print("\nBot detenido limpiamente.")
            break
        except Exception as e:
            time.sleep(3)


if __name__ == "__main__":
    run_polling()
