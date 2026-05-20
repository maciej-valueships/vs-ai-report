# vs-ai-report

Valueships report: **What is the real economic value of AI?**

- **Live site:** deployed on [Vercel](https://vercel.com) (see project `vs-ai-report`)
- **Source:** `demystifying-the-value-of-ai.md`
- **Build:** `python3 build_branded_html.py` → `index.html` (Vercel entry), `demystifying-ai-shareable.html` (CMS bundle)

## Local preview

```bash
python3 -m pip install -r requirements.txt
python3 build_branded_html.py
python3 -m http.server 8080
# open http://localhost:8080
```

## Deploy

Push to GitHub, then connect the repo in Vercel (or run `npx vercel --prod` from this directory).

Chapter CTAs link to [Valueships contact](https://www.valueships.com/contact).
