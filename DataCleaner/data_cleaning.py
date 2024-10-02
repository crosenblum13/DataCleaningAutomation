def clean_whitespace(df, columns):
    """
    Cleans trailing and double whitespaces from specified columns in a DataFrame.
    """
    try:
        for column in columns:
            if column in df.columns:
                df[column] = df[column].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
        return df
    except Exception as e:
        print(f"Error cleaning whitespace: {e}")
        return df


def drop_columns(df, columns_to_drop):
    """
    Drops the specified columns from the DataFrame.
    """
    try:
        df = df.drop(columns=columns_to_drop, errors='ignore')
        print("Dropped specified columns successfully.")
        return df
    except Exception as e:
        print(f"Error dropping columns: {e}")
        return df


def drop_first_row(df):
    """
    Drops the first row (index 0) from the DataFrame.
    """
    try:
        df = df.drop(index=0)
        print("Dropped the first row successfully.")
        return df
    except Exception as e:
        print(f"Error dropping the first row: {e}")
        return df


def clean_data(df):
    """
    Complete data cleaning function:
    - Drops row 0
    - Drops specified columns
    - Cleans trailing/double whitespaces for specified columns
    """
    # Columns to drop
    columns_to_drop = [
        "OR YTD", "Avg. Open Rate", "vs Target % - OR YTD", "CTR YTD", "Avg. Ctr",
        "vs Target % - CTR YTD", "CTOR YTD", "Avg. Target - CTOR", "vs Target % - CTOR YTD",
        "UR_YTD", "Orders - Open Ecomm YTD", "CVR - Open Ecomm YTD", "CVR - Open Ecomm YTD LOB",
        "Avg. Target - Ecomm CVR", "vs Target % - CVR eComm YTD", "Quantity - Open Ecomm YTD",
        "Sales - Open Ecomm YTD", "Quantity - Open Registration YTD", "CVR - Open Reg YTD",
        "CVR - Open Reg YTD LOB", "Avg. Cvr", "vs Target % - CVR Reg YTD", "Orders - Click Ecomm YTD",
        "CVR - Click Ecomm YTD", "Quantity - Click Ecomm YTD", "Sales - Click Ecomm YTD",
        "RPM - Click Ecomm YTD", "Quantity - Click Registration YTD", "CVR - Click Reg YTD"
    ]

    # Columns to clean for whitespace
    columns_to_clean = ['Ecomm/SEA', 'Week of Deployment Date', 'Deployment Date', 'Cid',
                        ' Email Type ', 'Program Name', 'Delivery Label', 'Version',
                        'Sline', 'Segment Code', 'Audience Segment']

    # Step 1: Drop the first row
    df = drop_first_row(df)

    # Step 2: Drop the specified columns
    df = drop_columns(df, columns_to_drop)

    # Step 3: Clean the specified columns for whitespace
    df = clean_whitespace(df, columns_to_clean)

    return df
