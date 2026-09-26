import argparse
import csv
import datetime
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("csv-summary")


def main():
    parser = argparse.ArgumentParser(description="Summarise an expenses CSV by category")
    parser.add_argument("--input", default="/data/expenses.csv")
    parser.add_argument("--output", default="/data/summary.txt")
    args = parser.parse_args()

    log.info("Starting csv-summary")
    log.info("Reading %s", args.input)

    try:
        f = open(args.input, newline="")
    except FileNotFoundError:
        log.error("Input file not found: %s", args.input)
        sys.exit(1)

    totals = {}
    count = 0
    with f:
        for row in csv.DictReader(f):
            try:
                amount = float(row["amount"])
                category = row["category"]
            except (KeyError, ValueError):
                log.warning("Skipping bad row: %s", row)
                continue
            totals[category] = totals.get(category, 0) + amount
            count += 1

    lines = [f"Summary generated {datetime.datetime.now().isoformat(timespec='seconds')}",
             f"Rows processed: {count}"]
    for category, total in sorted(totals.items()):
        lines.append(f"{category}: ${total:.2f}")
    lines.append(f"TOTAL: ${sum(totals.values()):.2f}")

    with open(args.output, "a") as out:
        out.write("\n".join(lines) + "\n\n")

    for line in lines:
        log.info(line)
    log.info("Report appended to %s", args.output)
    log.info("Finished successfully")


if __name__ == "__main__":
    main()