# Equity Research Generator - Developer Guide

## Project Structure

```
equity-research-generator/
├── src/                           # Main source code
│   ├── __init__.py
│   ├── main.py                   # Main orchestrator
│   ├── config.py                 # Configuration management
│   ├── models.py                 # Data models (Pydantic)
│   ├── data_fetchers.py          # Data collection from APIs
│   ├── analysis.py               # Analysis engines
│   └── report_generator.py       # Report building & export
│
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── test_data_fetchers.py     # Data fetcher tests
│   ├── test_analysis.py          # Analysis tests
│   └── test_report_generator.py  # Report generation tests
│
├── examples/                      # Example workflows
│   ├── workflows.py              # Complete workflow examples
│   └── sample_data.py            # Sample data for testing
│
├── docs/                         # Documentation
│   ├── GUIDE.md                 # This file
│   ├── API.md                   # API documentation
│   └── ARCHITECTURE.md          # Architecture details
│
├── reports/                      # Generated reports (output)
├── cache/                        # Cache directory
├── .env.example                  # Environment template
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── README.md                     # Main readme
└── pytest.ini                    # Pytest configuration
```

## Core Components

### 1. Configuration (`src/config.py`)

Manages all application settings using Pydantic:

```python
from src.config import settings

# Access settings
print(settings.sec_api_key)
print(settings.report_output_dir)
print(settings.llm_model)
```

**Key Settings:**
- API Keys (SEC, OpenAI, Finnhub, News API)
- Database configuration
- Output directories
- LLM parameters
- Review workflow settings

### 2. Data Models (`src/models.py`)

All data structures use Pydantic for validation:

```python
from src.models import (
    ResearchReport, InvestmentThesis, Citation,
    FinancialMetric, BusinessDriver, RiskFactor,
    NewsHighlight, ReportReviewRequest
)

# Create models with validation
report = ResearchReport(
    report_id="AAPL-001",
    ticker="AAPL",
    company_name="Apple Inc.",
    # ... other required fields
)

# Automatic validation and serialization
report_json = report.model_dump_json()
report_dict = report.model_dump()
```

**Key Models:**
- `ResearchReport` - Complete report with all sections
- `InvestmentThesis` - Investment perspective
- `Citation` - Traceable source references
- `FinancialMetric` - Historical metrics data
- `BusinessDriver` - Revenue stream analysis
- `RiskFactor` - Risk assessment
- `NewsHighlight` - Recent developments

### 3. Data Fetchers (`src/data_fetchers.py`)

Collects data from external sources:

```python
from src.data_fetchers import (
    SECFilingFetcher, FinancialDataFetcher,
    NewsAggregator, DocumentCache
)

# SEC filings
sec_fetcher = SECFilingFetcher(api_key=settings.sec_api_key)
filings = sec_fetcher.get_company_filings("AAPL")

# Financial data
fin_fetcher = FinancialDataFetcher(finnhub_key=settings.finnhub_api_key)
metrics = fin_fetcher.get_financial_metrics("AAPL")
prices = fin_fetcher.get_historical_prices("AAPL")

# News aggregation
news_agg = NewsAggregator(news_api_key=settings.news_api_key)
articles = news_agg.get_company_news("AAPL", "Apple Inc.")

# Caching
cache = DocumentCache(settings.cache_path)
cache.set("key", data)
cached_data = cache.get("key")
```

**Extending with New Sources:**

```python
class NewDataFetcher:
    """Add new data source"""
    def __init__(self, api_key):
        self.api_key = api_key
    
    def fetch_data(self, ticker):
        # Implement fetching logic
        return processed_data
```

### 4. Analysis Modules (`src/analysis.py`)

Processes raw data into insights:

```python
from src.analysis import (
    FinancialAnalyzer, BusinessDriverAnalyzer,
    RiskAnalyzer, SentimentAnalyzer,
    ValuationAnalyzer
)

# Financial analysis
fin_analyzer = FinancialAnalyzer()
metrics = fin_analyzer.extract_metrics(financial_data)
trends = fin_analyzer.calculate_trends(metrics)

# Business drivers
biz_analyzer = BusinessDriverAnalyzer()
drivers = biz_analyzer.analyze_drivers(overview, financial_data)

# Risk analysis
risk_analyzer = RiskAnalyzer()
risks = risk_analyzer.extract_risks(company_data, news_data)

# Sentiment analysis
sentiment_analyzer = SentimentAnalyzer()
result = sentiment_analyzer.analyze_sentiment(text)
highlights = sentiment_analyzer.analyze_news_sentiment(articles)

# Valuation
val_analyzer = ValuationAnalyzer()
metrics = val_analyzer.calculate_valuation_metrics(financial_data)
```

**Creating Custom Analyzers:**

```python
class CompetitorAnalyzer:
    """Custom analyzer for competitor analysis"""
    
    def analyze_competitive_landscape(self, company_data):
        # Extract competitors
        # Analyze market share
        # Compare metrics
        return competitors_analysis
```

### 5. Report Generation (`src/report_generator.py`)

Generates and exports reports:

```python
from src.report_generator import ReportGenerator, ReviewWorkflow

# Generate
generator = ReportGenerator()
report = generator.generate_report(
    ticker="AAPL",
    company_name="Apple Inc.",
    company_overview="Tech company...",
    # ... other data
)

# Export
generator.export_report(report, format="markdown")
generator.export_report(report, format="json")

# Review workflow
workflow = ReviewWorkflow()
workflow.submit_for_review(report, "Reviewer Name")
workflow.approve_report(report_id, "Reviewer")
workflow.reject_report(report_id, "Reviewer", "Reason")
```

### 6. Main Orchestrator (`src/main.py`)

Coordinates the entire pipeline:

```python
from src.main import EquityResearchGenerator

generator = EquityResearchGenerator()

# Generate complete report
report = generator.generate_report(
    ticker="AAPL",
    output_formats=["markdown", "json"],
    refresh_data=True,
    analyst_name="Team"
)

# Manage reviews
generator.get_pending_reviews()
generator.approve_report(report_id, reviewer_name)
generator.reject_report(report_id, reviewer_name, reason)
```

## Development Workflow

### 1. Setting Up Development Environment

```bash
# Clone and setup
git clone https://github.com/Samsonchau05/equity-research-generator.git
cd equity-research-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### 2. Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test class
pytest tests/test_analysis.py::TestFinancialAnalyzer -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Watch mode (requires pytest-watch)
ptw tests/
```

### 3. Running Examples

```bash
# Run all examples
python examples/workflows.py

# Run specific report generation
python src/main.py AAPL
```

### 4. Adding New Features

**Example: Add new data source**

1. Create fetcher in `src/data_fetchers.py`:
```python
class NewSourceFetcher:
    def fetch_data(self, ticker):
        # Implementation
        pass
```

2. Add to `src/main.py`:
```python
self.new_fetcher = NewSourceFetcher()
```

3. Use in `_collect_data()` method

4. Add tests in `tests/test_data_fetchers.py`

**Example: Add new analysis**

1. Create analyzer in `src/analysis.py`:
```python
class NewAnalyzer:
    def analyze(self, data):
        # Implementation
        pass
```

2. Add to report building in `src/report_generator.py`

3. Update report structure in `src/models.py`

4. Add tests in `tests/test_analysis.py`

## Common Tasks

### Generate a Report Programmatically

```python
from src.main import EquityResearchGenerator

generator = EquityResearchGenerator()
report = generator.generate_report(
    ticker="MSFT",
    output_formats=["markdown"],
    analyst_name="Research Team"
)

# Access report data
print(report.ticker)
print(report.company_name)
print(report.investment_thesis.recommendation)
```

### Process Multiple Tickers

```python
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

for ticker in tickers:
    try:
        report = generator.generate_report(ticker=ticker)
        print(f"✅ {ticker}: {report.report_id}")
    except Exception as e:
        print(f"❌ {ticker}: {e}")
```

### Custom Report Modification

```python
# Generate base report
report = generator.generate_report(ticker="AAPL")

# Modify programmatically
report.investment_thesis.recommendation = "buy"
report.investment_thesis.price_target = 175.0

# Export modified report
generator.report_generator.export_report(report)
```

### Implement Review Approval

```python
# Get pending reviews
pending = generator.get_pending_reviews()

for review in pending:
    report_id = review['report_id']
    ticker = review['ticker']
    
    # Review logic here...
    
    if approved:
        generator.approve_report(
            report_id=report_id,
            reviewer_name="Jane Analyst",
            comments="Excellent analysis"
        )
    else:
        generator.reject_report(
            report_id=report_id,
            reviewer_name="Jane Analyst",
            reason="Needs more competitive analysis"
        )
```

## Best Practices

### 1. Error Handling

```python
from src.main import EquityResearchGenerator

generator = EquityResearchGenerator()

try:
    report = generator.generate_report(ticker="INVALID")
except ValueError as e:
    print(f"Invalid ticker: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 2. Logging

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Starting report generation")
logger.debug(f"Using ticker: {ticker}")
logger.warning("Missing API key")
logger.error("Failed to fetch data")
```

### 3. Configuration Management

```python
from src.config import settings

# Access settings
if settings.enable_review_workflow:
    # Handle review workflow
    pass

# Override for testing
import os
os.environ["REFRESH_DATA_ON_GENERATE"] = "false"
```

### 4. Testing New Features

```python
import pytest

def test_new_feature():
    """Test new feature with mock data"""
    from src.analysis import NewAnalyzer
    
    analyzer = NewAnalyzer()
    result = analyzer.analyze(mock_data)
    
    assert result is not None
    assert result["expected_field"] == "expected_value"
```

## Debugging

### Enable Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

generator = EquityResearchGenerator()
report = generator.generate_report(ticker="AAPL")
```

### Inspect Report Data

```python
# View complete report
import json
print(json.dumps(report.model_dump(), indent=2, default=str))

# Check specific sections
print(f"Metrics: {len(report.financial_metrics)}")
print(f"Risks: {len(report.risk_factors)}")
print(f"News: {len(report.news_highlights)}")
```

### Cache Debugging

```python
from src.data_fetchers import DocumentCache
from src.config import settings

cache = DocumentCache(settings.cache_path)

# Check cache contents
data = cache.get("AAPL_company_data")

# Clear cache
cache.clear_expired()
```

## Performance Optimization

### 1. Caching Strategy

```python
# Use cache for repeated reports on same ticker
report1 = generator.generate_report("AAPL", refresh_data=False)
report2 = generator.generate_report("AAPL", refresh_data=False)

# Both use cached data for speed
```

### 2. Batch Processing

```python
# Process multiple tickers efficiently
for ticker in ["AAPL", "MSFT", "GOOGL"]:
    report = generator.generate_report(ticker)
    # Reports generated sequentially
```

### 3. Parallel Processing (Future)

```python
# Could implement with concurrent.futures or asyncio
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(generator.generate_report, ticker)
        for ticker in tickers
    ]
    reports = [f.result() for f in futures]
```

## Security Considerations

### API Key Management

```python
# ✅ Use environment variables
from src.config import settings
api_key = settings.openai_api_key

# ❌ Never hardcode keys
api_key = "sk-1234567890"  # WRONG

# ❌ Never commit .env file
git add .env  # WRONG
```

### Data Privacy

- Cache directory should be in `.gitignore`
- Sensitive data not logged to stdout
- Reports handled securely in production

## Troubleshooting

### Common Issues

**Missing API Keys**
```
Solution: Set all required keys in .env file
```

**Cache not updating**
```
Solution: Set CACHE_EXPIRY_HOURS=0 or delete cache files
```

**Report generation slow**
```
Solution: Use refresh_data=False to use cache
```

**Tests failing**
```
Solution: Run pytest -v to see detailed output
```

## Contributing Guidelines

1. Fork the repository
2. Create feature branch
3. Add tests for new features
4. Ensure all tests pass
5. Submit pull request

---

**Last Updated:** 2025-01-29  
**Version:** 0.1.0
