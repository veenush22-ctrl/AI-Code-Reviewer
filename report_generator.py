from datetime import datetime


def generate_report(code, results):
    """Generate a professional text report for the code analysis."""

    report = []

    report.append("=" * 70)
    report.append("AI CODE REVIEWER - CODE ANALYSIS REPORT")
    report.append("=" * 70)
    report.append("")

    report.append(
        f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    report.append("")

    report.append("-" * 70)
    report.append("1. ANALYSIS SUMMARY")
    report.append("-" * 70)

    flake8_result = results.get("flake8", "")
    black_result = results.get("black", "")
    radon_result = results.get("radon", "")

    if "No Flake8 issues found" in flake8_result:
        flake8_status = "PASS"
    else:
        flake8_status = "ISSUES FOUND"

    if "properly formatted" in black_result:
        black_status = "PASS"
    else:
        black_status = "FORMATTING SUGGESTIONS"

    report.append(f"Flake8 Status : {flake8_status}")
    report.append(f"Black Status  : {black_status}")

    report.append("")

    report.append("-" * 70)
    report.append("2. FLAKE8 CODE QUALITY ANALYSIS")
    report.append("-" * 70)
    report.append(flake8_result)

    report.append("")

    report.append("-" * 70)
    report.append("3. BLACK FORMATTING ANALYSIS")
    report.append("-" * 70)
    report.append(black_result)

    report.append("")

    report.append("-" * 70)
    report.append("4. RADON COMPLEXITY ANALYSIS")
    report.append("-" * 70)
    report.append(radon_result)

    report.append("")

    report.append("-" * 70)
    report.append("5. RECOMMENDATIONS")
    report.append("-" * 70)

    if flake8_status == "PASS" and black_status == "PASS":
        report.append(
            "✓ Code follows the checked style and formatting standards."
        )
        report.append(
            "✓ Continue following Python best practices and maintainable coding practices."
        )
    else:
        report.append(
            "• Review the Flake8 issues and resolve reported warnings/errors."
        )
        report.append(
            "• Apply Black formatting recommendations where required."
        )
        report.append(
            "• Review Radon complexity results and simplify highly complex functions."
        )

    report.append("")

    report.append("-" * 70)
    report.append("6. PROJECT INFORMATION")
    report.append("-" * 70)
    report.append(
        "This report was generated using the AI Code Reviewer."
    )
    report.append(
        "The tool analyzes Python code quality, formatting, and complexity."
    )

    report.append("")
    report.append("=" * 70)
    report.append("END OF REPORT")
    report.append("=" * 70)

    return "\n".join(report)


def save_report(report, filename="code_analysis_report.txt"):
    """Save the generated report to a text file."""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    return filename