def safe_divide(numerator, denominator):
    """
    Safely divides two numbers and returns 0 if there is any error (e.g., division by zero).
    """
    try:
        return numerator / denominator if denominator != 0 else 0
    except (ZeroDivisionError, TypeError):
        return 0


def add_calculations(df):
    """
    Adds calculated metric columns to the DataFrame with error handling.
    """
    try:
        df['OR'] = df.apply(lambda row: safe_divide(row['Opens_YTD'], row['Sent']), axis=1)
        df['CTR'] = df.apply(lambda row: safe_divide(row['Clicks_YTD'], row['Sent']), axis=1)
        df['CTOR'] = df.apply(lambda row: safe_divide(row['Clicks_YTD'], row['Opens_YTD']), axis=1)
        df['UR'] = df.apply(lambda row: safe_divide(row['Unsubs_YTD'], row['Opens_YTD']), axis=1)
        df['CVR'] = df.apply(lambda row: safe_divide(row['Quantity - Open Registration YTD LOB'], row['Opens_YTD']), axis=1)
        df['S.com CVR'] = df.apply(lambda row: safe_divide(row['Orders - Open Ecomm YTD LOB'], row['Opens_YTD']), axis=1)
        df['Quantity S.com CVR'] = df.apply(lambda row: safe_divide(row['Quantity - Open Ecomm YTD LOB'], row['Opens_YTD']), axis=1)
        df['AOV'] = df.apply(lambda row: safe_divide(row['Sales - Open Ecomm YTD LOB'], row['Quantity - Open Ecomm YTD LOB']), axis=1)

        print("Calculations added successfully with error handling.")
        return df
    except Exception as e:
        print(f"Error adding calculations: {e}")
        return df
