import streamlit as st
from analyzer import analyze_code
from report_generator import generate_report


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🔍",
    layout="wide"
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🔍 AI Code Reviewer")

st.markdown(
    """
    ### Intelligent Python Code Quality & Complexity Analyzer

    Upload a Python file to evaluate its **code quality,
    formatting, complexity, and maintainability** using
    automated Python analysis tools.
    """
)

st.divider()


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Analysis Tools")

    st.markdown(
        """
        **Enabled Analysis**

        ✅ Flake8  
        ✅ Black  
        ✅ Radon  

        ---

        **Supported File**

        `.py`

        ---

        **Output**

        📊 Quality Score  
        🔍 Code Quality Results  
        💡 Recommendations  
        📄 Downloadable Report
        """
    )


# ---------------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload your Python file",
    type=["py"],
    help="Upload a Python (.py) file for analysis."
)


# ---------------------------------------------------------
# MAIN ANALYSIS
# ---------------------------------------------------------

if uploaded_file is not None:

    try:

        code = uploaded_file.read().decode("utf-8")

        st.success(
            f"Successfully uploaded: {uploaded_file.name}"
        )

        st.divider()

        # -------------------------------------------------
        # CODE PREVIEW
        # -------------------------------------------------

        st.subheader("📝 Uploaded Code")

        with st.expander(
            "View Python Code",
            expanded=True
        ):

            st.code(
                code,
                language="python"
            )

        st.divider()

        # -------------------------------------------------
        # ANALYZE BUTTON
        # -------------------------------------------------

        if st.button(
            "🔍 Analyze Code",
            type="primary",
            use_container_width=True
        ):

            with st.spinner(
                "Analyzing your Python code..."
            ):

                results = analyze_code(code)

            st.success(
                "Code analysis completed successfully!"
            )

            st.divider()

            # -------------------------------------------------
            # QUALITY SCORE
            # -------------------------------------------------

            st.subheader("🎯 Overall Code Quality Score")

            score = results["score"]
            rating = results["rating"]

            score_col, rating_col = st.columns(2)

            with score_col:

                st.metric(
                    "Quality Score",
                    f"{score}/100"
                )

            with rating_col:

                st.metric(
                    "Code Quality Rating",
                    rating
                )

            if score >= 90:

                st.success(
                    "🌟 Excellent code quality."
                )

            elif score >= 75:

                st.success(
                    "✅ Good code quality with minor improvements possible."
                )

            elif score >= 60:

                st.warning(
                    "⚠️ Fair code quality. Some improvements are recommended."
                )

            elif score >= 40:

                st.warning(
                    "🔧 Code needs improvement in quality, formatting, or complexity."
                )

            else:

                st.error(
                    "🚨 Significant code quality improvements are recommended."
                )

            st.progress(
                score / 100
            )

            st.caption(
                "Score is calculated from Flake8 issues, Black formatting, "
                "and Radon complexity analysis."
            )

            st.divider()

            # -------------------------------------------------
            # ANALYSIS SUMMARY
            # -------------------------------------------------

            st.subheader("📊 Analysis Summary")

            flake8_pass = (
                "No Flake8 issues found."
                in results["flake8"]
            )

            black_pass = (
                "properly formatted"
                in results["black"]
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                if flake8_pass:

                    st.metric(
                        "Flake8",
                        "PASS"
                    )

                else:

                    st.metric(
                        "Flake8",
                        "REVIEW"
                    )

            with col2:

                if black_pass:

                    st.metric(
                        "Black",
                        "PASS"
                    )

                else:

                    st.metric(
                        "Black",
                        "REVIEW"
                    )

            with col3:

                st.metric(
                    "Radon",
                    "ANALYZED"
                )

            st.divider()

            # -------------------------------------------------
            # FLAKE8
            # -------------------------------------------------

            st.subheader(
                "🔍 Flake8 Code Quality Analysis"
            )

            if flake8_pass:

                st.success(
                    "✓ No Flake8 issues found."
                )

            else:

                st.warning(
                    "Flake8 reported issues that should be reviewed."
                )

                st.code(
                    results["flake8"],
                    language="text"
                )

            st.divider()

            # -------------------------------------------------
            # BLACK
            # -------------------------------------------------

            st.subheader(
                "🧹 Black Formatting Analysis"
            )

            if black_pass:

                st.success(
                    "✓ Code is properly formatted according to Black."
                )

            else:

                st.warning(
                    "Black identified formatting improvements."
                )

                st.code(
                    results["black"],
                    language="text"
                )

            st.divider()

            # -------------------------------------------------
            # RADON
            # -------------------------------------------------

            st.subheader(
                "📈 Radon Complexity Analysis"
            )

            st.code(
                results["radon"],
                language="text"
            )

            st.divider()

            # -------------------------------------------------
            # RECOMMENDATIONS
            # -------------------------------------------------

            st.subheader(
                "💡 Improvement Recommendations"
            )

            if flake8_pass and black_pass:

                st.success(
                    """
                    ✓ Code follows the checked style and formatting standards.

                    ✓ Continue following Python best practices.

                    ✓ Maintain readable and modular code.

                    ✓ Keep functions simple and maintainable.
                    """
                )

            else:

                st.info(
                    """
                    • Review Flake8 warnings and errors.

                    • Apply Black formatting recommendations.

                    • Review Radon complexity results.

                    • Simplify highly complex functions where possible.

                    • Follow clean and maintainable Python coding practices.
                    """
                )

            st.divider()

            # -------------------------------------------------
            # REPORT GENERATION
            # -------------------------------------------------

            report = generate_report(
                code,
                results
            )

            st.subheader(
                "📄 Analysis Report"
            )

            st.download_button(
                label="⬇️ Download Analysis Report",
                data=report,
                file_name="code_analysis_report.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.success(
                "Your analysis report is ready to download."
            )

    except UnicodeDecodeError:

        st.error(
            "Unable to read this file. "
            "Please upload a valid UTF-8 Python file."
        )

    except Exception as e:

        st.error(
            f"An unexpected error occurred: {str(e)}"
        )


# ---------------------------------------------------------
# DEFAULT SCREEN
# ---------------------------------------------------------

else:

    st.info(
        "👆 Upload a Python (.py) file above to begin the analysis."
    )

    st.markdown(
        """
        ### How It Works

        **1️⃣ Upload**  
        Select a Python source file.

        **2️⃣ Analyze**  
        Run automated code quality checks.

        **3️⃣ Score**  
        Get an overall code quality score out of 100.

        **4️⃣ Review**  
        Examine style, formatting and complexity results.

        **5️⃣ Improve**  
        Follow the generated recommendations.

        **6️⃣ Export**  
        Download the complete analysis report.
        """
    )