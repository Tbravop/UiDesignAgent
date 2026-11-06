---
name: visual-clustering
description: Skill técnica para extraer propiedades computadas y agrupamiento visual vía Playwright.
---

# Visual Clustering Skill — Playwright Execution

Skill técnica para extraer propiedades computadas vía Playwright.

```javascript
async function extractAndClusterElements(page) {
  return await page.evaluate(() => {
    const elements = Array.from(document.querySelectorAll('button, a, div, span, h1, h2, h3, p, input'));
    const clusters = {};

    elements.forEach((el) => {
      const rect = el.getBoundingClientRect();
      if (rect.width === 0 || rect.height === 0 || window.getComputedStyle(el).display === 'none') return;

      const style = window.getComputedStyle(el);
      const visualProperties = {
        backgroundColor: style.backgroundColor,
        color: style.color,
        fontSize: style.fontSize,
        fontWeight: style.fontWeight,
        borderRadius: style.borderRadius,
        paddingTop: style.paddingTop,
        paddingRight: style.paddingRight,
        paddingBottom: style.paddingBottom,
        paddingLeft: style.paddingLeft
      };

      const styleFingerprint = JSON.stringify(visualProperties);
      if (!clusters[styleFingerprint]) {
        clusters[styleFingerprint] = { fingerprint: styleFingerprint, count: 1, sampleTagName: el.tagName.toLowerCase() };
      } else {
        clusters[styleFingerprint].count++;
      }
    });
    return Object.values(clusters);
  });
}
```

## Python Playwright Native Runner
```python
from playwright.sync_api import sync_playwright

def cluster_live_page(url="http://localhost:8000/index.html"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(url, wait_until="networkidle")
        # Invoca la función evaluate anterior
        browser.close()
```