from playwright.sync_api import sync_playwright

URL = "https://publicacionesprocesales.ramajudicial.gov.co/web/publicaciones-procesales/inicio"

playwright = sync_playwright().start()

# 👇 ÚNICO CAMBIO: usar Chrome del sistema
browser = playwright.chromium.launch(
    headless=False,
    channel="chrome"
)

def abrir_juzgado(juzgado):
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded")

    selects = page.locator(".select2-selection")

    # ===== DEPARTAMENTO =====
    selects.nth(0).click()
    page.locator(
        ".select2-results__option",
        has_text=juzgado["departamento"]
    ).first.click()

    # ⏳ esperar carga de filtros dependientes
    page.wait_for_timeout(900)

    # ===== MUNICIPIO (SI EXISTE) =====
    if juzgado.get("municipio"):
        selects.nth(1).click()
        page.wait_for_selector(".select2-results__option")

        page.locator(
            ".select2-results__option",
            has_text=juzgado["municipio"]
        ).first.click()

        page.wait_for_timeout(900)

    # ⏳ esperar ENTIDAD y ESPECIALIDAD
    page.wait_for_timeout(1200)

    # ===== DESPACHO = ÚLTIMO SELECT =====
    total_selects = selects.count()
    despacho_select = selects.nth(total_selects - 1)

    despacho_select.click()

    search = page.locator(".select2-search__field")
    search.wait_for(state="visible")
    search.fill(juzgado["despacho"])

    page.wait_for_timeout(800)
    page.locator(".select2-results__option").first.click()

    # ===== BUSCAR =====
    page.get_by_role("button", name="Buscar").click()
