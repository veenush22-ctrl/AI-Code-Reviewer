import subprocess
import tempfile
import os
import sys
import re


def run_command(command):
    """Run a command and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )

        return result.stdout + result.stderr

    except subprocess.TimeoutExpired:
        return "Analysis timed out."

    except Exception as e:
        return f"Error while running analysis: {str(e)}"


def analyze_with_flake8(code):
    """Analyze Python code using Flake8."""

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as temp_file:

        temp_file.write(code)
        file_path = temp_file.name

    try:
        output = run_command(
            [sys.executable, "-m", "flake8", file_path]
        )

        if not output.strip():
            return "No Flake8 issues found."

        return output

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def analyze_with_black(code):
    """Check Python code formatting using Black."""

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as temp_file:

        temp_file.write(code)
        file_path = temp_file.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "black",
                "--check",
                file_path
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        output = result.stdout + result.stderr

        if result.returncode == 0:
            return "Code is properly formatted according to Black."

        return output

    except subprocess.TimeoutExpired:
        return "Black formatting check timed out."

    except Exception as e:
        return f"Black error: {str(e)}"

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def analyze_with_radon(code):
    """Analyze code complexity using Radon."""

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as temp_file:

        temp_file.write(code)
        file_path = temp_file.name

    try:
        output = run_command(
            [
                sys.executable,
                "-m",
                "radon",
                "cc",
                file_path,
                "-s"
            ]
        )

        if not output.strip():
            return "No complexity information available."

        return output

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def calculate_quality_score(results):
    """
    Calculate an overall code quality score out of 100.

    The score considers:
    - Flake8 issues
    - Black formatting
    - Radon complexity
    """

    score = 100

    flake8_result = results.get("flake8", "")
    black_result = results.get("black", "")
    radon_result = results.get("radon", "")

    # -----------------------------------------------------
    # FLAKE8 SCORE
    # -----------------------------------------------------

    if "No Flake8 issues found." not in flake8_result:

        flake8_lines = [
            line
            for line in flake8_result.splitlines()
            if line.strip()
        ]

        issue_count = len(flake8_lines)

        flake8_penalty = min(issue_count * 4, 40)

        score -= flake8_penalty

    # -----------------------------------------------------
    # BLACK SCORE
    # -----------------------------------------------------

    if "properly formatted" not in black_result:

        score -= 10

    # -----------------------------------------------------
    # RADON SCORE
    # -----------------------------------------------------

    complexity_values = []

    matches = re.findall(
        r"\(([0-9]+)\)",
        radon_result
    )

    for value in matches:
        try:
            complexity_values.append(int(value))
        except ValueError:
            pass

    if complexity_values:

        max_complexity = max(complexity_values)

        if max_complexity <= 5:
            score -= 0

        elif max_complexity <= 10:
            score -= 10

        elif max_complexity <= 20:
            score -= 20

        else:
            score -= 30

    # -----------------------------------------------------
    # FINAL SCORE
    # -----------------------------------------------------

    score = max(0, min(100, score))

    if score >= 90:
        rating = "Excellent"

    elif score >= 75:
        rating = "Good"

    elif score >= 60:
        rating = "Fair"

    elif score >= 40:
        rating = "Needs Improvement"

    else:
        rating = "Poor"

    return score, rating


def analyze_code(code):
    """Run complete code quality analysis."""

    flake8_result = analyze_with_flake8(code)
    black_result = analyze_with_black(code)
    radon_result = analyze_with_radon(code)

    results = {
        "flake8": flake8_result,
        "black": black_result,
        "radon": radon_result
    }

    score, rating = calculate_quality_score(results)

    results["score"] = score
    results["rating"] = rating

    return results