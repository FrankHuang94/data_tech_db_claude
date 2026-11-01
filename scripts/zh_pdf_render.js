// Render the Chinese-edition HTML book to PDF with Chromium (Playwright).
// Usage: node scripts/zh_pdf_render.js <book.html> <out.pdf>
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [, , htmlPath, outPath] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load', timeout: 0 });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: outPath,
    format: 'A4',
    printBackground: true,
    outline: true,
    tagged: false,
    displayHeaderFooter: true,
    margin: { top: '20mm', bottom: '18mm', left: '18mm', right: '18mm' },
    headerTemplate: '<div style="width:100%;font-size:7.5px;color:#888;padding:0 18mm;font-family:\'Noto Sans SC\',\'WenQuanYi Zen Hei\',sans-serif;text-align:right;">AI 数据图谱（AI Data Atlas）· 简体中文参考译本</div>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#666;text-align:center;font-family:\'Noto Sans SC\',\'WenQuanYi Zen Hei\',sans-serif;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    timeout: 0,
  });
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
