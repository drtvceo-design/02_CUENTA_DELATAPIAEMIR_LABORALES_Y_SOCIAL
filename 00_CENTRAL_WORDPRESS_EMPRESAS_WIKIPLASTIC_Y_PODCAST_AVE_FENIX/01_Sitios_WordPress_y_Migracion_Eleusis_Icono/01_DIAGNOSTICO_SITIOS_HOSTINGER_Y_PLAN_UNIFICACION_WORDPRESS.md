# Diagnóstico Técnico de Sitios en Hostinger, Migración de `eleusis-icono.com` (Horizons → WordPress) y Arquitectura de Páginas por Empresa

**Fecha de auditoría en vivo:** 15 de noviembre de 2026  
**Método de verificación:** Inspección HTTP/2 externa + auditoría SSH de solo lectura (`ssh hostinger-kuchiuyas` → `/home/u485132360/domains/`) + WP-CLI no destructivo.  
**Cortafuegos de privacidad aplicado:** CERO modificaciones destructivas en servidor, CERO exposición de correos privados, CERO claves o tokens en plantillas públicas y aislamiento estricto de asuntos procesales.

---

## 1. Diagnóstico Real en Vivo de los Sitios en Hostinger (`/home/u485132360/domains/`)

Todos los dominios auditados responden **`HTTP 200 OK`** con certificado TLS válido. A continuación se presenta la radiografía técnica exacta verificada hoy en el servidor:

| # | Dominio / Sitio | Estado HTTP | Motor / Versión | Tema Activo | Plugins de Correo, Formularios y E-Commerce | Páginas Principales Publicadas | Privacidad `author=1` (`display_name` / `nicename`) | Diagnóstico y Acción Recomendada |
|---|---|---|---|---|---|---|---|---|
| **1** | `https://eleusis-icono.com` *(Externo a `/domains/`, alojado en Hostinger Horizons)* | `200 OK` (`0,27 s`) | **Hostinger Horizons AI** (SPA React + Vite) | Tailwind oscuro/cian compilado | Sin formulario real (solo `mailto:` y marcador `+591 700 00000`) | `/` (6 tarjetas Bento), `/subsidiaries` (4 S.R.L.), `/contact` | Metadato público `Eleusis Ícono S.A.` | **Respaldo 100% completado** en [respaldo_eleusis_icono_horizons/](file:///Users/kuchimac/.gemini/antigravity/scratch/00_PROYECTOS_POR_NUREJ/02_CUENTA_DELATAPIAEMIR_LABORALES_Y_SOCIAL/00_CENTRAL_WORDPRESS_EMPRESAS_WIKIPLASTIC_Y_PODCAST_AVE_FENIX/01_Sitios_WordPress_y_Migracion_Eleusis_Icono/respaldo_eleusis_icono_horizons). Listo para migrar a WordPress con control total. |
| **2** | `https://info.universolife.com` | `200 OK` (`1,15 s`) | **WordPress `7.1.4`** | `twentytwentyfive` (`1.5`) | `hostinger-reach` (`1.8.10`), `jetpack` (`16.4`), `google-site-kit` (`1.191.0`) | `ID 68` (*Universo Life · Hub Central* — Portada), `ID 122` (*Investigación: Grafeno y Sostenibilidad*), `ID 51` (*Grafeno y Materiales Avanzados*) + 5 entradas | **Protegido:** `AVA · Universo Life` (`ava-universo-life`) | **Excelente estado.** Núcleo y plugins al día. Candidato ideal de referencia técnica (WordPress 7.1.4 + tema de bloques `twentytwentyfive`). |
| **3** | `https://index.universolife.com` | `200 OK` (`1,17 s`) | **WordPress `6.8.12`** | `hostinger-ai-theme` (`1.0.63`) | `hostinger-reach` (`1.4.12`), `wordpress-mcp` (`0.2.4`), `google-site-kit` | Muestra últimas entradas en portada; páginas `ID 9` (*Índice Fiduciario Panas Token*), `ID 5` (*Bienvenido*), `ID 3` (*Privacy Policy*) | **Protegido:** `Universo Life Hub` (`universo-life-hub`) | Actualizar núcleo a WP `7.1.4`, fijar `ID 9` como portada estática e instalar `Forminator` o `WP Mail SMTP` si recibirá consultas. |
| **4** | `https://casa-red.universolife.com` | `200 OK` (`1,11 s`) | **WordPress `7.1.4`** | `hostinger-ai-theme` (`1.0.63`) | `hostinger-reach` (`1.4.12`), `wordpress-mcp` (`0.2.4`), `google-site-kit` | `ID 5` (*Inicio* — Portada), `ID 6` (*Divisiones y Servicios*), `ID 7` (*Proceso de Tokenización y Estructuración*), `ID 8` (*Gobernanza y Beneficios*), `ID 3` (*Política de Privacidad*) | **Protegido:** `Editorial Casa Red` (`editorial-casa-red`) | **Intacto y respetado** (sin tocar pestañas ni borradores). Añadir bloque QR SEPREC `RGYC7EFWG7` y botones WhatsApp corporativos. |
| **5** | `https://token.drtapiavargas.com` | `200 OK` (`1,38 s`) | **WordPress `6.8.12`** | `hostinger-ai-theme` (`1.0.63`) | `hostinger-reach` (`1.4.12`), `wordpress-mcp` (`0.2.4`) | `ID 9` (*Home* — Portada, título *Sorteo vaser mundialista*), `ID 10` (*Tokens*), `ID 11` (*Services*), `ID 12` (*Nfts*), `ID 25/26` (*Call Back*) | **Protegido:** `División Tokens Eleusis` (`tokens-eleusis`) | Actualizar WP a `7.1.4` y renombrar el título del sitio a **Portal Oficial de Tokens & RWA · Ecosistema Algorand**. |
| **6** | `https://karapanza.in` | `200 OK` (`1,54 s`) | **WordPress `7.1.4`** | `blocksy` (`2.1.60`) + `blocksy-companion` | `woocommerce` (`11.3.0`), `hostinger-reach` (`1.8.7`) | Muestra entradas vacías en portada (`show_on_front: posts`, `0` posts); páginas publicadas: `ID 5` (*Tienda*), `ID 6` (*Carrito*), `ID 7` (*Finalizar compra*), `ID 8` (*Mi cuenta*) | `admin-tapia` (`admin-tapia`) — conviene cambiar `display_name` a `Editorial Karapanza` | **Acción clave:** Asignar una portada comercial real (o la *Tienda* `ID 5` + catálogo de **Bebidas Kuchiuyas / ALKA El Romeral**) e integrar pasarela QR Bolivia + WhatsApp. |
| **7** | `https://shop.boliviachic.com` | `200 OK` (`1,33 s`) | **WordPress `7.1.4`** | `hostinger-ai-theme` (`1.0.63`) | `woocommerce` (`11.3.0`), `nowpayments-for-woocommerce` (`1.4.1`), `jetpack` (`16.4`) | `ID 19` (*Fábrica de Bloques & Tienda de Tokens Bolivia* — Portada), `ID 6` (*Tienda*), `ID 7` (*Carrito*), `ID 8` (*Finalizar compra*), `ID 9` (*Mi cuenta*) | **Protegido:** `Tienda BoliviaChic` (`tienda-boliviachic`) | **Operativo con pasarela cripto NOWPayments.** Ideal para venta internacional de NFTs Kuchiuyas, ediciones coleccionables y merchandising. |
| **8** | `https://formulario.drtapiavargas.com` | `200 OK` (`0,78 s`) | **Estático por defecto** (`default.php` de Hostinger, sin WP) | Página placeholder de Hostinger (`16.369 bytes`, abr. 2025) | Ninguno aún | Solo `default.php` (*Default page*) | N/A | **¡Oportunidad de oro!** Este subdominio está libre y listo para alojar el **Portal Oficial del Tamiz Inteligente 2027** (Residentes `WikiPlastic` + Preselección Quirúrgica Enero 2027). |
| **9** | `https://eleusis.apple-war.com` | `200 OK` (`1,17 s`) | **WordPress `6.8.12`** | `hostinger-ai-theme` (`1.0.63`) | `hostinger-reach` (`1.4.12`), `google-site-kit` | `ID 9` (*Home* — *ELEUSIS – Graphenic Blockchain Hub*), `ID 10` (*Ecosystem*), `ID 11` (*Technology*), `ID 12` (*Sustainability*), `ID 3` (*Privacy Policy*) | **Protegido:** `Eleusis Ícono` (`eleusis-icono`) | Actualizar a WP `7.1.4` y enlazar bidireccionalmente con `info.universolife.com` y `eleusis-icono.com`. |
| **10** | `https://porno.kuchiuyas.com` | `200 OK` (`0,93 s`) | **WordPress `7.1.4`** | `twentytwentyfive` (`1.5`) | `forminator` (`1.58.4`), `woocommerce` (`11.3.0`), `nowpayments`, `coinpayments`, `defender-security` (`6.4.1`), `hostinger-reach`, `wordpress-popup` | `ID 9` (*Crónicas Picarescas de Los Kuchiuyas* — Portada), `ID 124` (*Generar Historias Kuchiuyas*), `ID 10` (*Blog*), `ID 63` (*Shop*) + 4 crónicas | **Protegido:** `Dr. Aquiles Castro Vergara` (`aquiles-castro-vergara`) | **El sitio más blindado y completo del servidor** (tiene `Forminator` + `Defender Security` + doble pasarela cripto). Sirve de modelo exacto de plugins para los demás sitios. |

### Sitios Complementarios Detectados en `/home/u485132360/domains/`
- **`https://api.universolife.com`** (`200 OK`, PHP nativo seguro): Aloja `ava_vivo.php`, `familia.php`, `refugio.php` e `index.php` (Cabina Viva AVA/Serena).
- **`https://civitai.kuchiuyas.com`** (`200 OK`, WP `6.8.12`): Galería de modelos y generación audiovisual IA (*Civitai Kuchiuyas IA*).
- **`https://api.karapanza.in`** (`200 OK`, WP `6.8.12`): *API Médica de Interacción* (base ideal para conectar o redirigir a **`WikiPlastic`**).
- **`https://coral-woodpecker-688846.hostingersite.com`** (`200 OK`, WP `6.8.12`): Staging temporal *ELEUSIS* que puede servir como **banco de pruebas previo** antes de apuntar el DNS definitivo de `eleusis-icono.com` a WordPress.

### Hallazgo Crítico sobre Correo y Formularios en WordPress
1. Actualmente **solo `porno.kuchiuyas.com` tiene instalado `Forminator` (`1.58.4`)** para formularios interactivos estructurados; el resto solo tiene `hostinger-reach` (captación básica de boletines).
2. Ninguno de los WordPress tiene aún un plugin SMTP dedicado (`FluentSMTP` o `WP Mail SMTP`), por lo que dependen de `php mail()` local de Hostinger. Además, como se verificó en `hpanel.hostinger.com`, el buzón corporativo requiere reactivar con un clic el envío saliente en hPanel para despachar notificaciones transaccionales con firma `DKIM/SPF` perfecta desde `@eleusis-icono.com` y `@drtapiavargas.com`.

---

## 2. Guía Paso a Paso para Migrar `eleusis-icono.com` de Hostinger Horizons a WordPress (100% Bajo Tu Control)

### ¿Por qué salir de Hostinger Horizons hacia WordPress?
En **Hostinger Horizons**, la web es una aplicación cerrada compilada en un único archivo JavaScript minificado (`452 KB`): cada cambio depende de gastar créditos del generador IA de Hostinger, no tiene páginas individuales indexables en Google por empresa, tenía botones sociales vacíos (`#`) y un teléfono marcador (`+591 700 00000`).  
Al pasarla a **WordPress (`twentytwentyfive` + Editor de Bloques)** en tu mismo plan Hostinger:
- Eres **100% dueño del código, base de datos MariaDB y archivos** vía `ssh hostinger-kuchiuyas` y `wp-cli`.
- Cada empresa tiene su propia URL limpia (`/eleusis-icono`, `/panacea-icono`, `/casared`, `/el-centenial`, `/bomgo-club`, `/salar-opulence`, `/vaser-lipo-center`, `/jardineria-paisajismo`) posicionando en Google por nombre societario y rubro.
- Nuestros agentes nocturnos (`webmaster-hostinger`) pueden actualizar precios, catálogos, noticias o códigos QR en segundos sin gastar créditos de Horizons.

### Procedimiento Seguro en 5 Pasos (Cero Tiempo Fuera de Línea)
1. **Respaldo previo garantizado (YA HECHO HOY):** Todo el HTML, JS, CSS y las 10 imágenes originales de Horizons ya están guardados en [respaldo_eleusis_icono_horizons/](file:///Users/kuchimac/.gemini/antigravity/scratch/00_PROYECTOS_POR_NUREJ/02_CUENTA_DELATAPIAEMIR_LABORALES_Y_SOCIAL/00_CENTRAL_WORDPRESS_EMPRESAS_WIKIPLASTIC_Y_PODCAST_AVE_FENIX/01_Sitios_WordPress_y_Migracion_Eleusis_Icono/respaldo_eleusis_icono_horizons).
2. **Pre-armado en Staging (`coral-woodpecker-688846.hostingersite.com`):**
   - Actualizar ese staging a WordPress `7.1.4` y activar el tema nativo de bloques `twentytwentyfive`.
   - Subir las 10 imágenes rescatadas (`horizons_images/`) a la Biblioteca de Medios de WordPress.
   - Importar en la página de Inicio el archivo listo [plantilla_hub_eleusis_y_empresas_wordpress.html](file:///Users/kuchimac/.gemini/antigravity/scratch/00_PROYECTOS_POR_NUREJ/02_CUENTA_DELATAPIAEMIR_LABORALES_Y_SOCIAL/00_CENTRAL_WORDPRESS_EMPRESAS_WIKIPLASTIC_Y_PODCAST_AVE_FENIX/01_Sitios_WordPress_y_Migracion_Eleusis_Icono/plantilla_hub_eleusis_y_empresas_wordpress.html) (en el Editor de Bloques: menú `⋮` arriba a la derecha → **Editor de código** → pegar el contenido íntegro → volver a **Editor visual** → Guardar).
3. **Creación de las 8 Páginas Individuales y Redirecciones Limpias:**
   - Crear las páginas `/subsidiaries` (redirigida o integrada al directorio de empresas) y `/contact` para no romper ningún enlace compartido previamente desde Horizons.
4. **Cambio de Destino en hPanel (`eleusis-icono.com`):**
   - En `hpanel.hostinger.com` → *Sitios Web*, desvincular `eleusis-icono.com` de la instancia Horizons y asignarlo como dominio principal sobre el directorio WordPress `/home/u485132360/domains/eleusis-icono.com/public_html` ejecutando `wp search-replace` desde el staging.
5. **Blindaje de Seguridad, Correo y Privacidad:**
   - Enmascarar `author=1` con `display_name = "Consejo Editorial Eleusis Ícono"` y `user_nicename = "editorial-eleusis"`.
   - Instalar `Defender Security`, `LiteSpeed Cache`, `Forminator` y `FluentSMTP` conectado a `contacto@eleusis-icono.com`.

---

## 3. Arquitectura Detallada de Página Individual por Empresa y Unidad Operativa

Cada una de las **8 páginas corporativas individuales** dentro de `eleusis-icono.com` (y espejadas en sus portales específicos cuando aplique) sigue un **Estándar Único de Confianza Institucional y Conversión en 5 Bloques**:

1. **Bloque 1 — Cabecera de Identidad Corporativa (Hero):** Logotipo oficial, denominación legal exacta, lema de valor y botón primario de contacto directo por WhatsApp corporativo.
2. **Bloque 2 — Objeto Social Comercial y Líneas de Servicio Activas (2026–2027):** Qué resuelve para clientes, aliados o inversionistas en lenguaje ejecutivo claro.
3. **Bloque 3 — Bloque de Transparencia Registral SEPREC con Verificación QR en 3 Segundos:** Tarjeta técnica con número de Matrícula de Comercio / NIT, número de Certificado SEPREC vigente, código alfanumérico QR oficial e imagen del código QR escaneable con cualquier celular para comprobar su vigencia registral en menos de 3 segundos ante el portal oficial del SEPREC / DIRNOPLU, sin exponer jamás documentos privados ni controversias judiciales.
4. **Bloque 4 — Portafolio / Catálogo o Enlace a Plataforma Operativa:** Conexión directa al e-commerce, plataforma tecnológica o formulario de preselección.
5. **Bloque 5 — Doble Botón de WhatsApp Corporativo (Coordinación con Pamela):**
   - **Línea Corporativa 1:** `+591 77122210` (`https://wa.me/59177122210`)
   - **Línea Corporativa 2:** `+591 76123237` (`https://wa.me/59176123237`)
   - Cada botón lleva un mensaje prellenado (`?text=...`) que identifica de inmediato desde qué empresa escribe el cliente para que Pamela clasifique y atienda en segundos.

### Fichas Maestras de las 8 Páginas Individuales

#### 3.1. `eleusis-icono.com/eleusis-icono/` — Asociación Accidental «ELEUSIS ÍCONO» & Matriz Estratégica
- **Posicionamiento:** Arquitectura empresarial, articulación de consorcios de innovación, economía regenerativa del grafeno boliviano, I+D+i y gobierno corporativo.
- **Secciones clave:** Ecosistema interconectado de divisiones; Economía Circular y Materiales Avanzados (enlace a `info.universolife.com/investigacion`); Alianzas institucionales e inversión en activos reales (RWA).
- **Bloque Transparencia SEPREC (3 segundos):**
  - *Instrumento:* Escritura Pública N° `116/2026`
  - *Certificado SEPREC:* N° `1167778/2026` · **Código QR SEPREC:** `901A4BUK1U`
  - *Representación Común Inscrita:* Sr. Iván Luna Arias (Poder General N° `167/2026` · Reg. SEPREC `852460`).
- **CTA WhatsApp:** `?text=Hola%2C%20solicito%20informaci%C3%B3n%20institucional%20de%20ELEUSIS%20%C3%8DCONO` (`+591 77122210` / `+591 76123237`).

#### 3.2. `eleusis-icono.com/panacea-icono/` — Asociación Accidental «PANACEA ÍCONO»
- **Posicionamiento:** Laboratorio de inteligencia artificial multimodal, educación médica digital (`WikiPlastic`), automatización conversacional (16 bots especializados en Telegram + Cabina AVA) y Web3 sobre Algorand.
- **Secciones clave:** Suite de Asistentes IA y Bots públicos (`@ELEUSIS_BOT`, `@Panas_token_bot`, `@DRAQUILES_bot`); Tokenización utilitaria y cultural (`Panas Token`, `RDA8`, NFTs ARC-3); Producción audiovisual transmedia y Podcast *«El Ave Fénix»*.
- **Bloque Transparencia SEPREC (3 segundos):**
  - *Instrumento:* Escritura Pública N° `117/2026`
  - *Certificado SEPREC:* N° `1167791/2026` · **Código QR SEPREC:** `7UX1K2IF0A`
- **CTA WhatsApp:** `?text=Hola%2C%20deseo%20informaci%C3%B3n%20tecnol%C3%B3gica%20de%20PANACEA%20%C3%8DCONO` (`+591 76123237` / `+591 77122210`).

#### 3.3. `eleusis-icono.com/casared/` — `CASARED S.R.L.` (Sincronizada con `casa-red.universolife.com`)
- **Posicionamiento:** Infraestructura de redes, gestión inmobiliaria inteligente, avalúos periciales de arquitectura/ingeniería, estructuración de activos inmobiliarios tokenizados y hábitat conectado.
- **Secciones clave:** Administración y desarrollo patrimonial urbano; Domótica y conectividad residencial/corporativa; Integración con la Unidad de Paisajismo y Diseño de Exteriores.
- **Bloque Transparencia SEPREC (3 segundos):**
  - *Matrícula SEPREC y NIT:* `474366027`
  - *Certificado SEPREC:* N° `1135597/2026` · **Código QR SEPREC:** `RGYC7EFWG7`
  - *Poder Especial Inscrito:* N° `186/2026` (Reg. SEPREC `1243050`, QR `DF8UK6GZOG`).
- **CTA WhatsApp:** `?text=Hola%2C%20solicito%20servicios%20inmobiliarios%20o%20t%C3%A9cnicos%20de%20CASARED%20S.R.L.` (`+591 77122210` / `+591 76123237`).

#### 3.4. `eleusis-icono.com/el-centenial/` — `EL CENTENIAL S.R.L.` · Biotecnología & Hacienda El Romeral
- **Posicionamiento:** Laboratorio biotecnológico de química verde, planta piloto en el Fundo Rústico **Hacienda El Romeral**, desarrollo de formulaciones botánicas alcalinas (`ALKA`) y gestión de programas ejecutivos de salud y bienestar quirúrgico boutique 2027.
- **Secciones clave:** Línea Biotecnológica y Fitofarmacéutica `ALKA El Romeral`; Patrocinio de Investigación Clínica y Desarrollo Sostenible; Coordinación de paquetes integrales de bienestar y recuperación Enero 2027.
- **Bloque Transparencia SEPREC (3 segundos):**
  - *Matrícula SEPREC y NIT:* `471860025`
  - *Certificado SEPREC:* N° `1136039/2026` · **Código QR SEPREC:** `KTAA2YCNIA`
  - *Ampliación de Objeto Social:* Testimonio N° `99/2026` · **QR DIRNOPLU:** `EMCPJWBbZ4ff`
- **CTA WhatsApp:** `?text=Hola%2C%20consulta%20para%20EL%20CENTENIAL%20S.R.L.%20y%20Proyecto%20ALKA%20El%20Romeral` (`+591 76123237` / `+591 77122210`).

#### 3.5. `eleusis-icono.com/bomgo-club/` — `BOMGO CLUB S.R.L.`
- **Posicionamiento:** Ecosistema gastronómico de autor, coctelería conceptual, club de experiencias sensoriales privadas, noches de arte/jazz/podcast en vivo y sede oficial del **Ritual de Cata de los 7 Pecados Kuchiuyas**.
- **Secciones clave:** Experiencias privadas por reserva; Maridaje andino-contemporáneo con elixires `ALKA El Romeral`; Eventos corporativos y lanzamientos culturales en Sucre.
- **Bloque Transparencia SEPREC (3 segundos):**
  - *Matrícula SEPREC y NIT:* `473564020`
  - *Certificado SEPREC:* N° `1135005/2026` · **Código QR SEPREC:** `VMNQ1r6dDz73`
- **CTA WhatsApp:** `?text=Hola%2C%20deseo%20reservar%20mesa%20o%20evento%20en%20BOMGO%20CLUB%20S.R.L.` (`+591 77122210` / `+591 76123237`).

#### 3.6. `eleusis-icono.com/salar-opulence/` — `SALAR OPULENCE LIQUORS S.R.L.`
- **Posicionamiento:** Casa de destilados de lujo, licores de autor inspirados en la pureza mineral de los Andes y los valles de Chuquisaca, botellas numeradas coleccionables y **Bebidas Personalizadas por Personaje y Pecado Kuchiuya** con gemelo digital NFT en Algorand.
- **Secciones clave:** Colección *Hacienda El Romeral*; Colección *Los 7 Pecados Capitales & Redención (Los Kuchiuyas)*; Test interactivo *«Descubre tu Elixir Personalizado»* conectado a `karapanza.in` y `shop.boliviachic.com`.
- **Bloque Transparencia SEPREC (3 segundos):**
  - *Matrícula SEPREC y NIT:* `514480025`
  - *Certificado SEPREC:* N° `1101970/2026` · **Código QR SEPREC:** `EKBB22LGVK`
- **CTA WhatsApp:** `?text=Hola%2C%20deseo%20adquirir%20destilados%20de%20SALAR%20OPULENCE%20LIQUORS%20S.R.L.` (`+591 76123237` / `+591 77122210`).

#### 3.7. `eleusis-icono.com/vaser-lipo-center/` — `VASER LIPO CENTER S.R.L.` *(Nota expresa de Autonomía Societaria)*
- **Posicionamiento:** Centro hospitalario quirúrgico de **3° Nivel de Atención** en Sucre (Calle Colón N° 526), referente en cirugía plástica estética y reconstructiva, contorno corporal ultrasónico de alta definición, hospitalización segura y docencia quirúrgica clínica.
- **Cláusula Pública de Claridad Institucional:** Se consigna de manera limpia y transparente que `VASER LIPO CENTER S.R.L.` es una **sociedad comercial independiente y autónoma** (que no forma parte de las Asociaciones Accidentales del holding comercial), con gobierno societario, patrimonio y representación legal propios inscritos en el SEPREC.
- **Secciones clave:** Infraestructura hospitalaria de 3° Nivel y bioseguridad; Acceso al **Tamiz Inteligente de Preselección de Pacientes Enero 2027** (`formulario.drtapiavargas.com`); Enlace educativo a `WikiPlastic`.
- **Bloque Transparencia SEPREC y Sanitaria (3 segundos):**
  - *Matrícula SEPREC y NIT:* `183728027`
  - *Certificado SEPREC:* N° `1176350/2026` · **Código QR SEPREC:** `GX5X12Y891`
  - *Representante Legal Vigente:* Lic. Marvin Gilmar Medrano Chamoso (Poder Especial N° `224/2026`, QR DIRNOPLU `F37moRvsfJC2`)
  - *Habilitación Sanitaria Oficial:* Resolución Administrativa SEDES-CH N° `2/2025` (Establecimiento de Salud de 3° Nivel, vigente al `07/07/2027`).
- **CTA WhatsApp:** `?text=Hola%2C%20solicito%20informaci%C3%B3n%20del%20Tamiz%20de%20Preselecci%C3%B3n%20Quir%C3%BArgica%20Enero%202027` (`+591 77122210` / `+591 76123237`).

#### 3.8. `eleusis-icono.com/jardineria-paisajismo/` — Unidad de Jardinería, Vivero Botánico & Paisajismo Bioclimático
- **Posicionamiento:** Unidad especializada de diseño paisajístico, arquitectura verde exterior, jardines contemplativos y terapéuticos, vivero de especies ornamentales y aromáticas en **Hacienda El Romeral**, y mantenimiento integral de condominios, clínicas, hoteles y residencias en Sucre y valles de Chuquisaca.
- **Activos Fotográficos Reales Disponibles:** Respaldada por las **36 fotografías reales de campo en alta resolución (`Octubre 2026`)** localizadas en `/Users/kuchimac/Mi unidad/Proyecto jardinería `, listas para galería comparativa de *Antes / Diseño / Ejecución*.
- **Paquetes Comerciales Estructurados para Venta Inmediata:**
  1. *Plan Residencial / Condominio Mensual:* Poda técnica, nutrición orgánica de suelos, control fitosanitario ecológico y reposición floral de estación.
  2. *Jardines Bioclimáticos & Terapéuticos de Autor:* Diseño estético inspirado en proporción áurea, piedra natural chuquisaqueña, especies nativas de bajo consumo hídrico y aromáticas del Romeral (romero, lavanda, muña, cedrón).
  3. *Provisión de Vivero & Huertos Botánicos:* Plantines seleccionados, sustratos enriquecidos y asesoría agronómica.
- **Respaldo Registral Operativo:** Facturación y contratación formal bajo **CASARED S.R.L.** (`QR RGYC7EFWG7` — obras exteriores y mantenimiento inmobiliario) y **EL CENTENIAL S.R.L.** (`QR KTAA2YCNIA` — producción botánica Hacienda El Romeral).
- **CTA WhatsApp:** `?text=Hola%2C%20deseo%20agendar%20visita%20t%C3%A9cnica%20de%20Jardiner%C3%ADa%20y%20Paisajismo` (`+591 76123237` / `+591 77122210`).
