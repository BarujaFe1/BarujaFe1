<div align="center">

# Felipe Baruja

**Construtor de Sistemas de Dados, Produtos Full-Stack & Engenharia Agentic**  
*Graduando em Estatística e Ciência de Dados pela Universidade de São Paulo (USP)*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/barujafe/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BarujaFe1)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:felipebaruja@usp.br)

<p align="center">
  Trabalho na interseção entre <strong>rigor estatístico</strong>, <strong>engenharia de software robusta</strong> e <strong>sistemas autônomos de IA</strong>.<br/>
  Do design de experimentos e inferência causal à arquitetura de dados, sistemas offline-first e interfaces de alto impacto visual.
</p>

---

</div>

## 🧭 Princípios de Engenharia & Filosofia de Trabalho

- 🔬 **Evidence Before Claims**: Protocolo estrito anti-overclaim — *Static Code ≠ Unit Test ≠ Live Integration ≠ Production*. Nenhuma métrica é afirmada sem prova empírica.
- 📐 **Estatística Sem Vazamento (Zero Leakage)**: Separação temporal estrita em séries temporais, inferência com incerteza explícita (intervalos críveis/confiança) e controle metodológico rigoroso.
- 📶 **Offline-First & Resiliência Real**: Arquiteturas que operam sem conexão (IndexedDB/SQLite local via Dexie/Expo) com filas de mutação idempotentes e conciliação assíncrona.
- ⚡ **Qualidade em Escada (Test Ladder)**: TDD orientado a domínio, testes unitários rápidos, validações de contrato de API, testes E2E com Playwright e linters de alta velocidade (Biome).

---

## 🚀 Vitrine de Projetos em Destaque

### 📊 Estatística Aplicada, Causalidade & Risco Operacional
| Projeto | Descrição & Arquitetura | Stack & Tecnologias | Repositório |
| :--- | :--- | :--- | :---: |
| **CausalForge** | Laboratório de inferência causal aplicada a decisões de negócio (Diff-in-Diff, matching, incerteza explicável e decision memos). | `FastAPI` `Next.js` `SciPy` `Statsmodels` | [Código](https://github.com/BarujaFe1/CausalForge) |
| **RiskShield** | Review board para governança de scores analíticos, calibração de thresholds, subgrupos, explicabilidade e registro de risco. | `Next.js` `TypeScript` `Recharts` | [Código](https://github.com/BarujaFe1/RiskShield) |
| **ForecastOps** | Forecasting operacional com modelagem de incerteza: baselines de séries temporais, backtesting temporal e simulações what-if. | `TypeScript` `React` `D3` | [Código](https://github.com/BarujaFe1/ForecastOps) · [Demo](https://barujafe1.github.io/ForecastOps/) |
| **ProcessLens** | Mineração de processos para logs de eventos operacionais — descoberta de DFG, detecção de gargalos, retrabalho e variantes de casos. | `FastAPI` `Next.js` `Graphviz` | [Código](https://github.com/BarujaFe1/ProcessLens) |
| **SentinelaSUS** | Painel de vigilância epidemiológica sintética com sinais estatísticos interpretáveis e monitoramento de anomalias regionais. | `FastAPI` `Next.js` `Pandas` | [Código](https://github.com/BarujaFe1/SentinelaSUS) |

---

### 🛡️ DataOps, Confiabilidade & Observabilidade de Dados
| Projeto | Descrição & Arquitetura | Stack & Tecnologias | Repositório |
| :--- | :--- | :--- | :---: |
| **DataFlow** | Lab local-first de qualidade de dados: data profiling explicável, score de confiabilidade estatística e mascaramento consciente de LGPD. | `Next.js` `FastAPI` `SciPy` `Tailwind` | [Código](https://github.com/BarujaFe1/DataFlow) · [Demo](https://dataflow-sand.vercel.app) |
| **metric-contract-studio** | Estúdio de governança e contratos de métricas corporativas: taxonomia, validação de fórmulas, scoring e export para engenharia analítica. | `Next.js` `TypeScript` `Tailwind` | [Código](https://github.com/BarujaFe1/metric-contract-studio) · [Demo](https://metric-contract-studio.vercel.app) |
| **dataops-control-tower** | Torre de controle de observabilidade de dados: detecção de schema drift, SLAs de pipelines, freshness e gestão de incidentes. | `Next.js` `TypeScript` `Zod` | [Código](https://github.com/BarujaFe1/dataops-control-tower) · [Demo](https://dataops-control-tower.vercel.app) |
| **ReconcileIQ** | Motor de conciliação financeira de pedidos, liquidações e taxas com pareamento exato/fuzzy e caixa prioritária de exceções. | `FastAPI` `Next.js` `PostgreSQL` | [Código](https://github.com/BarujaFe1/ReconcileIQ) |
| **JobScope-Tech** | Grafo de coocorrência de competências técnicas em vagas reais de tecnologia e dados (Greenhouse/Lever) comparado com portfólio. | `TypeScript` `React` `NetworkX` | [Código](https://github.com/BarujaFe1/JobScope-Tech) · [Demo](https://jobscope-signal-graph-baruja-fe.vercel.app) |

---

### 📱 Full-Stack, Mobile & Sistemas Offline-First
| Projeto | Descrição & Arquitetura | Stack & Tecnologias | Repositório |
| :--- | :--- | :--- | :---: |
| **LancaEnsaio** | App móvel de campo para lançamento padronizado de ensaios agrícolas: auditoria contínua, fila de mutações offline e sync com Supabase. | `Expo` `React Native` `Supabase` | [Código](https://github.com/BarujaFe1/LancaEnsaio) · [Demo](https://lancaensaio.vercel.app) |
| **fueltrack-pro** | App mobile offline-first para gestão de consumo de combustível (km/L) e custos de frotas com banco SQLite local e testes Vitest. | `React Native` `Expo` `SQLite` `Vitest` | [Código](https://github.com/BarujaFe1/fueltrack-pro) |
| **Verbo & Hino** | Aplicativo multiplataforma de quizzes e gamificação do conhecimento bíblico com modos clássico, relógio e persistência offline. | `React Native` `Expo` `TypeScript` | [Código](https://github.com/BarujaFe1/VerboHino) |
| **Soniva** | Software desktop local-first para ingestão, preservação de metadados e indexação rápida de acervos de áudio. | `Tauri` `Rust` `React` `SQLite` | [Código](https://github.com/BarujaFe1/Soniva) |

---

### ✨ Conceitos Comerciais & Experiências Digitais (Next.js + Tailwind)
| Projeto | Proposta de Design & Valor Comercial | Destaques de Engenharia | Repositório |
| :--- | :--- | :--- | :---: |
| **ana-paula-japur-conceito** | Presença institucional acolhedora e refinada para psicologia clínica. | Tipografia editorial, agendamento ágil e pontuação máxima no Lighthouse. | [Código](https://github.com/BarujaFe1/ana-paula-japur-conceito) |
| **dinamica-conceito** | Protótipo comercial B2B para engenharia de software e produtos sob medida. | Design industrial, simulação de escopo e conversão ágil. | [Código](https://github.com/BarujaFe1/dinamica-conceito) |
| **potenza-conceito** | Conceito corporativo de alto impacto visual para catálogo de equipamentos. | Componentização modular, performance visual e design responsivo. | [Código](https://github.com/BarujaFe1/potenza-conceito) |
| **cidade-pet-spa** | Plataforma mobile-first para agendamento de estética e bem-estar animal. | Catálogo dinâmico por porte de pet e integração direta ao WhatsApp. | [Código](https://github.com/BarujaFe1/cidade-pet-spa) |
| **pedra-belli-conceito** | Mostruário digital e galeria de arquitetura para revestimentos nobres. | Otimização de imagens de alta resolução e transições suaves. | [Código](https://github.com/BarujaFe1/pedra-belli-conceito) |

---

## 🛠️ Stack Tecnológica & Ferramentas

```text
Linguagens       :: TypeScript • JavaScript • Python • SQL • Bash • Rust (básico)
Frontend & UI    :: React • Next.js (App Router) • Tailwind CSS • Radix UI • Lucide • Framer Motion
Mobile & Desktop :: Expo • React Native • Tauri (Rust/Web) • SQLite nativo
Backend & APIs   :: Node.js • FastAPI • RESTful • Supabase • PostgreSQL • Dexie (IndexedDB)
Dados & Ciência  :: Pandas • NumPy • SciPy • Statsmodels • Scikit-Learn • Jupyter Notebooks
Qualidade & QA   :: Vitest • Playwright • Jest • Biome • ESLint • Test-Driven Development (TDD)
DevOps & Tooling :: Git • GitHub Actions / CI • Docker • Linux (Ubuntu Workstation) • Vercel
Agentic AI       :: Google Antigravity • Autonomia Baseada em Evidência • Multi-agent Workflows
```

---

## 📈 Estatísticas do GitHub

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=BarujaFe1&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub Stats" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=BarujaFe1&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" width="48%" />
</div>

---

<div align="center">
  <sub>© 2026 <strong>Felipe Baruja</strong> — Conecte-se comigo no <a href="https://www.linkedin.com/in/barujafe/">LinkedIn</a> ou pelo e-mail <a href="mailto:felipebaruja@usp.br">felipebaruja@usp.br</a>.</sub>
</div>
