<!-- The images in assets/ are animated SVGs made by scripts/gen_assets.py (Python, no dependencies, no external services). Edit the text there and run it again. -->

<p align="center">
  <a href="https://fernandodevbrito.github.io/portfolio/">
    <img src="assets/header.svg" width="100%" alt="Fernando Brito. Full Stack Software Developer: .NET, C#, Angular, React, SQL Server and AI-assisted development. Open to remote roles, based in Aracaju, Brazil (UTC-3).">
  </a>
</p>

<p align="center">
  <a href="https://fernandodevbrito.github.io/portfolio/"><img src="https://img.shields.io/badge/Portfolio-13131A?style=for-the-badge" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/fernandobrito-dev"><img src="https://img.shields.io/badge/LinkedIn-13131A?style=for-the-badge" alt="LinkedIn"></a>
  <a href="https://fernandodevbrito.github.io/portfolio/assets/Fernando_Brito_Fullstack_Developer_EN.pdf"><img src="https://img.shields.io/badge/Resume_(PDF)-13131A?style=for-the-badge" alt="Resume (PDF)"></a>
  <a href="mailto:fernando.dev.brito@gmail.com"><img src="https://img.shields.io/badge/Email-13131A?style=for-the-badge" alt="Email"></a>
</p>

## About me

- Full Stack Software Developer with **4+ years** building and running a **nationwide B2B ERP** (fiscal, financial, billing, purchasing, inventory) at DP Sistemas, with **C#/.NET, Angular, React and SQL Server**.
- **Leading a team** of three junior developers and one intern since 2024.
- **Modernizing legacy code with AI:** moving a .NET Framework 4 / WebForms system to .NET 10 and React with coding agents, with lint and CI/CD in the loop and a human validating every change before it ships.
- Strong in **SQL Server tuning**, **RabbitMQ messaging**, third-party integrations and production incident response (**150+ incidents** resolved).
- Based in **Aracaju, Brazil (UTC-3)** · English **C1** · **open to remote roles**.

## Impact

<p align="center">
  <img src="assets/impact.svg" width="100%" alt="4+ years in production on a nationwide B2B ERP. 50k+ transactions a month through bank reconciliation. 10k+ e-invoices a month through the SEFAZ tax integration. 1M+ records migrated from legacy databases to SQL Server.">
</p>

## Featured project

<p align="center">
  <a href="https://github.com/FernandoDevBrito/lonerchestrator">
    <img src="assets/lonerchestrator.svg" width="100%" alt="Lonerchestrator pipeline: a card goes through split, plan, build, checks, review and merge, with a fix loop from review back to build (3 attempts max, then it asks a human).">
  </a>
</p>

**[Lonerchestrator](https://github.com/FernandoDevBrito/lonerchestrator)** is a local multi-agent orchestrator for AI coding agents, built with AI. You describe the work on a card; agents plan, implement, review and fix it on their own, and stop only when the card is approved or needs a human. Guardrails are checked by code, not prompts (protected files, diff size, secrets, deleted tests), and nothing merges until CI passes and two independent reviewers approve.

Open source (MIT) · one-line install on Windows, macOS and Linux · no API keys, no server.

<details>
<summary><b>See the board</b></summary>
<br>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/FernandoDevBrito/lonerchestrator/main/docs/images/board-dark.png">
  <img alt="The Lonerchestrator board in the browser: Backlog, In progress, Needs you and Done" src="https://raw.githubusercontent.com/FernandoDevBrito/lonerchestrator/main/docs/images/board-light.png" width="100%">
</picture>
</details>

## Selected work

<p align="center">
  <a href="https://fernandodevbrito.github.io/portfolio/#projects"><img src="assets/card-legacy.svg" width="49%" alt="Legacy Modernization with AI: a .NET Framework 4 and WebForms system moving to .NET 10 and React, with AI agents and human review of every change."></a>
  <a href="https://fernandodevbrito.github.io/portfolio/#projects"><img src="assets/card-etl.svg" width="49%" alt="ERP Data Migration: C# and Python ETL that moved 1M+ records from PostgreSQL, Oracle, MariaDB and Firebird into one SQL Server with 100% referential integrity."></a>
  <a href="https://fernandodevbrito.github.io/portfolio/#projects"><img src="assets/card-sefaz.svg" width="49%" alt="SEFAZ Fiscal Hub: Angular dashboard and C# .NET XML engine processing 10k+ e-invoices a month through SEFAZ web services."></a>
  <a href="https://github.com/FernandoDevBrito/Projeto_UK"><img src="assets/card-uk.svg" width="49%" alt="UK Police Analytics API: async FastAPI service that aggregates UK Police crime data with Pandas and maps it on a Leaflet dashboard."></a>
</p>

<p align="center"><sub>Production work at DP Sistemas is private, so those cards open the case studies on my portfolio. The UK Police API has a <a href="https://fernandodevbrito.github.io/Projeto_UK/frontend/index.html">live demo</a>.</sub></p>

## Tech stack

<table>
  <tr>
    <td><b>Backend</b></td>
    <td>
      <img src="https://img.shields.io/badge/C%23-13131A?style=for-the-badge" alt="C#">
      <img src="https://img.shields.io/badge/.NET-13131A?style=for-the-badge&logo=dotnet&logoColor=26D970" alt=".NET">
      <img src="https://img.shields.io/badge/ASP.NET_Core-13131A?style=for-the-badge&logo=dotnet&logoColor=26D970" alt="ASP.NET Core">
      <img src="https://img.shields.io/badge/Entity_Framework_Core-13131A?style=for-the-badge" alt="Entity Framework Core">
      <img src="https://img.shields.io/badge/Dapper-13131A?style=for-the-badge" alt="Dapper">
      <img src="https://img.shields.io/badge/Python-13131A?style=for-the-badge&logo=python&logoColor=26D970" alt="Python">
      <img src="https://img.shields.io/badge/FastAPI-13131A?style=for-the-badge&logo=fastapi&logoColor=26D970" alt="FastAPI">
    </td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td>
      <img src="https://img.shields.io/badge/Angular-13131A?style=for-the-badge&logo=angular&logoColor=26D970" alt="Angular">
      <img src="https://img.shields.io/badge/React-13131A?style=for-the-badge&logo=react&logoColor=26D970" alt="React">
      <img src="https://img.shields.io/badge/TypeScript-13131A?style=for-the-badge&logo=typescript&logoColor=26D970" alt="TypeScript">
      <img src="https://img.shields.io/badge/RxJS-13131A?style=for-the-badge&logo=reactivex&logoColor=26D970" alt="RxJS">
      <img src="https://img.shields.io/badge/HTML5-13131A?style=for-the-badge&logo=html5&logoColor=26D970" alt="HTML5">
      <img src="https://img.shields.io/badge/CSS-13131A?style=for-the-badge&logo=css&logoColor=26D970" alt="CSS">
      <img src="https://img.shields.io/badge/Tailwind_CSS-13131A?style=for-the-badge&logo=tailwindcss&logoColor=26D970" alt="Tailwind CSS">
    </td>
  </tr>
  <tr>
    <td><b>Data &amp; messaging</b></td>
    <td>
      <img src="https://img.shields.io/badge/SQL_Server-13131A?style=for-the-badge" alt="SQL Server">
      <img src="https://img.shields.io/badge/PostgreSQL-13131A?style=for-the-badge&logo=postgresql&logoColor=26D970" alt="PostgreSQL">
      <img src="https://img.shields.io/badge/Redis-13131A?style=for-the-badge&logo=redis&logoColor=26D970" alt="Redis">
      <img src="https://img.shields.io/badge/RabbitMQ-13131A?style=for-the-badge&logo=rabbitmq&logoColor=26D970" alt="RabbitMQ">
      <img src="https://img.shields.io/badge/MongoDB-13131A?style=for-the-badge&logo=mongodb&logoColor=26D970" alt="MongoDB">
    </td>
  </tr>
  <tr>
    <td><b>Cloud &amp; DevOps</b></td>
    <td>
      <img src="https://img.shields.io/badge/Docker-13131A?style=for-the-badge&logo=docker&logoColor=26D970" alt="Docker">
      <img src="https://img.shields.io/badge/Azure-13131A?style=for-the-badge" alt="Azure">
      <img src="https://img.shields.io/badge/Azure_DevOps-13131A?style=for-the-badge" alt="Azure DevOps">
      <img src="https://img.shields.io/badge/GitHub_Actions-13131A?style=for-the-badge&logo=githubactions&logoColor=26D970" alt="GitHub Actions">
      <img src="https://img.shields.io/badge/Git-13131A?style=for-the-badge&logo=git&logoColor=26D970" alt="Git">
      <img src="https://img.shields.io/badge/Linux-13131A?style=for-the-badge&logo=linux&logoColor=26D970" alt="Linux">
    </td>
  </tr>
  <tr>
    <td><b>Quality &amp; APIs</b></td>
    <td>
      <img src="https://img.shields.io/badge/xUnit-13131A?style=for-the-badge" alt="xUnit">
      <img src="https://img.shields.io/badge/Swagger-13131A?style=for-the-badge&logo=swagger&logoColor=26D970" alt="Swagger">
      <img src="https://img.shields.io/badge/JWT-13131A?style=for-the-badge&logo=jsonwebtokens&logoColor=26D970" alt="JWT">
      <img src="https://img.shields.io/badge/Postman-13131A?style=for-the-badge&logo=postman&logoColor=26D970" alt="Postman">
    </td>
  </tr>
  <tr>
    <td><b>AI-assisted dev</b></td>
    <td>
      <img src="https://img.shields.io/badge/Claude_Code-13131A?style=for-the-badge&logo=claude&logoColor=26D970" alt="Claude Code">
      <img src="https://img.shields.io/badge/Codex-13131A?style=for-the-badge" alt="Codex">
      <img src="https://img.shields.io/badge/Gemini-13131A?style=for-the-badge&logo=googlegemini&logoColor=26D970" alt="Gemini">
    </td>
  </tr>
</table>

## Let's talk

Looking for a **remote full stack or .NET role** with an international team. The fastest way to reach me is [email](mailto:fernando.dev.brito@gmail.com) or [LinkedIn](https://www.linkedin.com/in/fernandobrito-dev).

<p align="center">
  <img src="assets/footer.svg" width="100%" alt="fernando@brito:~$ echo &quot;thanks for stopping by&quot;">
</p>
