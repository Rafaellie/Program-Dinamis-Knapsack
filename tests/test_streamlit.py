def test_streamlit_runs():
    import importlib
    try:
        import streamlit_app
        importlib.reload(streamlit_app)
    except Exception as e:
        pytest.fail(f"Streamlit app failed to import or run: {e}")