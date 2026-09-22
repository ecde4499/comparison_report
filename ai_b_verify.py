from playwright.sync_api import sync_playwright
from pathlib import Path
import hashlib, json

html_text = Path('/mnt/data/task5_unpack/index.html').read_text(encoding='utf-8')
results=[]
errors=[]

def rec(tid, ok, detail):
    results.append({'id':tid,'status':'PASS' if ok else 'FAIL','detail':detail})

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1400,'height':1000})
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.add_init_script("""
      (() => {
        const store = {};
        Object.defineProperty(window, 'localStorage', {value: {
          getItem: k => Object.prototype.hasOwnProperty.call(store,k) ? store[k] : null,
          setItem: (k,v) => { store[k] = String(v); },
          removeItem: k => { delete store[k]; },
          clear: () => { for (const k of Object.keys(store)) delete store[k]; }
        }});
      })();
    """)
    page.set_content(html_text, wait_until='load')
    page.wait_for_timeout(50)
    txt=page.locator('#txt'); count=page.locator('#char-count'); ratio=page.locator('#ratio')

    txt.fill('안녕하세요')
    rec('T05-01', count.inner_text()=='5 / 200자', f"표시={count.inner_text()}")

    txt.fill('')
    rec('T05-02', count.inner_text()=='0 / 200자', f"표시={count.inner_text()}")

    txt.fill('가'*200)
    cls=count.get_attribute('class') or ''
    rec('T05-03', count.inner_text()=='200 / 200자' and 'warning' not in cls.split(), f"표시={count.inner_text()}, class={cls}")

    txt.fill('가'*201)
    cls=count.get_attribute('class') or ''
    rec('T05-04', count.inner_text()=='201 / 200자 (권장 초과)' and 'warning' in cls.split(), f"표시={count.inner_text()}, class={cls}")

    txt.fill('가'*100)
    cls=count.get_attribute('class') or ''
    rec('T05-05', count.inner_text()=='100 / 200자' and 'warning' not in cls.split(), f"표시={count.inner_text()}, class={cls}")

    txt.fill('가A1')
    rec('T05-06', count.inner_text()=='3 / 200자', f"표시={count.inner_text()}")

    txt.fill('😀😀')
    rec('T05-07', count.inner_text()=='2 / 200자', f"표시={count.inner_text()}")

    txt.fill('ABC\nDEF')
    rec('T05-08', count.inner_text()=='7 / 200자', f"표시={count.inner_text()}")

    keep='비율 유지 테스트😀'
    txt.fill(keep)
    base_count=count.inner_text()
    dims=[]; ok=True
    expected={'1:1':'900 × 900px · 1:1','4:5':'900 × 1125px · 4:5','9:16':'900 × 1600px · 9:16'}
    for r in ['1:1','4:5','9:16']:
        ratio.select_option(r)
        page.wait_for_timeout(20)
        dim=page.locator('#dim').inner_text(); dims.append(dim)
        ok = ok and txt.input_value()==keep and count.inner_text()==base_count and dim==expected[r]
    rec('T05-09', ok, f"문구={txt.input_value()!r}, 글자수={count.inner_text()}, dims={dims}")

    ratio.select_option('1:1')
    txt.fill('')
    before=page.locator('#c').evaluate("c=>c.toDataURL('image/png')")
    txt.fill('가'*201)
    page.wait_for_timeout(30)
    after=page.locator('#c').evaluate("c=>c.toDataURL('image/png')")
    after_count=count.inner_text()
    render_changed = hashlib.sha256(before.encode()).hexdigest()!=hashlib.sha256(after.encode()).hexdigest()
    rec('T05-10', render_changed and txt.input_value()==('가'*201) and after_count.startswith('201 / 200자') and not errors,
        f"canvas변경={render_changed}, 입력길이={len(txt.input_value())}, 표시={after_count}, JS오류={errors}")

    browser.close()

print(json.dumps({'results':results,'page_errors':errors},ensure_ascii=False,indent=2))
