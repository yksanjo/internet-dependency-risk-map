from datetime import datetime, timezone


def main() -> None:
    print("internet-dependency-risk-map initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
