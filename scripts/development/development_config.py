QeMLflow Development Configuration
===============================

Quick setup configuration for development features.
"""

import os

# Development settings
DEVELOPMENT_MODE = True
ENABLE_PERFORMANCE_MONITORING = True
AUTO_GENERATE_DOCS = True

# Paths
PROJECT_ROOT = Path(__file__).parent
PERFORMANCE_REPORTS_DIR = PROJECT_ROOT / "performance_reports"
API_DOCS_DIR = PROJECT_ROOT / "docs" / "api_auto"


# Quick setup function
def setup_development_environment():
    """Setup QeMLflow development environment with enhanced features."""

    print("🚀 Initializing QeMLflow development environment...")

    # Create necessary directories
    PERFORMANCE_REPORTS_DIR.mkdir(exist_ok=True)
    API_DOCS_DIR.mkdir(exist_ok=True)

    # Import and test core functionality
    try:
        import qemlflow

        print("✅ QeMLflow core imported successfully")

        # Test performance monitoring
        from qemlflow.core.monitoring import show_performance_dashboard

        print("✅ Performance monitoring available")

        # Test model recommendations
        from qemlflow.core.recommendations import recommend_model

        print("✅ Model recommendation system available")

        print("\n🎉 Development environment ready!")
        print("\nQuick commands:")
        print(
            "  📊 Performance dashboard: python -c 'from qemlflow.core.monitoring import show_performance_dashboard; show_performance_dashboard()'"
        )
        print(
            '  🤖 Model recommendation: python -c \'from qemlflow.core.recommendations import recommend_model; print(recommend_model(["CCO", "CCC"], "logP"))\''
        )
        print("  📚 API docs: open docs/api_auto/index.html")

        return True

    except ImportError as e:
        print(f"⚠️ Warning: Some features may not be available: {e}")
        return False


if __name__ == "__main__":
    setup_development_environment()
