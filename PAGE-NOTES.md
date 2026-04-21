# `real/index.html` — 页面说明与变更记录

本文档说明 `real/` 目录下落地页的目的、内容约定，以及近期为上线/整理所做过的修改，方便日后查阅。

## 文件与资源

| 文件 / 目录 | 说明 |
|-------------|------|
| `index.html` | 首页落地页（表格布局，无 Wayback/wombat 等归档脚本）。 |
| `hero.webp` | 顶部横幅图，页面中用 `./hero.webp` 引用。 |
| `sitemap-index.xml` | 站点地图索引，指向 `sitemap-pages.xml`（正式域名：`realtorsatthebeach.com`）。 |
| `sitemap-pages.xml` | 含首页与子站路径 URL：`/water-damage/`、`/siding-services/`、`/plumbing/`。 |
| `robots.txt` | 允许爬取全文并声明 Sitemap 地址。 |
| `water-damage/index.html` | 水损/霉菌专线占位页（与侧栏链接一致，避免仅上传首页时 404）。 |
| `siding-services/index.html` | 外立面维修占位页。 |
| `plumbing/index.html` | 管道类子站占位页（索引中有，主页未链出；可由 Worker 再接）。 |

### Cloudflare Pages 直传时把整个 `real` 文件夹拖进去

需包含：`index.html`、`hero.webp`、上述 sitemap / robots、三个子目录里的 `index.html`，这样根链与 `/water-damage/`、`/siding-services/` 在静态托管下也能打开；绑定 `realtorsatthebeach.com` 后，再把 `realtors-router` Worker 绑到 `realtorsatthebeach.com/*`（按你的 SOP）。

## 页面结构（概览）

1. **顶栏灰条**  
   文案：`REALTORS AT THE BEACH : Now Partnered with the National Property Protection Network`。

2. **副标题**  
   `Real Estate Agents Covering Myrtle Beach And The Entire Grand Strand Area!`

3. **主横幅**  
   本地 WebP 图 `hero.webp`（勿再改用临时生成的 JPG 版本）。

4. **主栏（约 640px）**  
   - 标题区：`Realtors In Myrtle Beach & The Grand Strand!`、SC Coastal Directory 链接、「Latest Added Showing First」。  
   - **经纪人列表**：保留原名、经纪公司、街道地址；外链仍为各站点上的 `VISIT PROFILE`。  
   - **Related Categories**：四类外链。  
   - **隐藏链**：全站地图 ` /sitemap-index.xml`（小字/隐藏块内，便于爬虫发现）。

5. **右侧栏（250px）**（自上而下）  
   - **This Week's Featured Profile**：Natalie Rakoci 大图（与列表同款 `250×250` 图源），可点击进入其资料页。  
   - **Emergency Dispatch Center**：24/7 电话 `+1 (607) 400-9375`，以及 `/water-damage/`、`/siding-services/` 两个站内路径链接。

## 近期会话中已落实的修改（备忘）

以下是为对齐产品图、去掉多余文件、恢复视觉完整性而做的工作：

1. **主图格式**  
   - 使用 **`hero.webp`** 作为横幅，不再使用曾临时生成的 `hero-beach.jpg`。  
   - 已删除已不再需要的转换脚本及 JPG 成品（若本地仍有旧文件，应以本说明为准统一为 WebP）。

2. **清理多余说明**  
   - 移除了页面上仅作内部说明用的 **「(archive toolbar/scripts removed)」** 一类文字，避免访客看到工程备注。

3. **右侧「特色简介」大图**  
   - 在保留 **Emergency Dispatch Center** 的前提下，**恢复了「This Week's Featured Profile」及 Natalie Rakoci 的大头像**，避免右侧只有红框、缺少原站常见的「特色人物」展示。

## 日后维护建议

- 换横幅：替换 `hero.webp` 并保持文件名，或同步修改 `index.html` 里 `<img src>`。  
- 改紧急调度文案/链接：只改右侧红框内对应 `div`。  
- 改特色人物：替换图源、标题、姓名行及 `href`，并保持与主列表中的经纪人信息一致（勿随意改名改址）。

---

*文档生成背景：2026-04-20 前后对 `real/index.html` 的整理与恢复说明；同年补充 sitemap、子路径占位与 robots，便于 Pages 上传。*
