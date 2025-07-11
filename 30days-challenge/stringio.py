from io import StringIO

def generate_report():
    output = StringIO()
    print("Report Header", file=output)
    print("=" * 20, file=output)
    print("Data: 123", file=output)
    return output.getvalue()

report = generate_report()  # Returns the full formatted string
print(report)
