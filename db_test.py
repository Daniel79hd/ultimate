#!/usr/bin/env python3
"""
Database connection test script
Tests database connectivity and basic operations
"""

import sqlite3
import sys
from datetime import datetime


def test_sqlite_connection():
    """Test SQLite database connection and basic operations"""
    print("=" * 50)
    print("Testing SQLite Database Connection")
    print("=" * 50)
    
    try:
        # Connect to SQLite database (creates file if doesn't exist)
        conn = sqlite3.connect('test_database.db')
        cursor = conn.cursor()
        
        print("✓ Connection established successfully")
        
        # Create a test table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("✓ Test table created")
        
        # Insert test data
        test_message = f"Database test at {datetime.now()}"
        cursor.execute(
            "INSERT INTO test_table (message) VALUES (?)",
            (test_message,)
        )
        conn.commit()
        print(f"✓ Test record inserted: {test_message}")
        
        # Query the data
        cursor.execute("SELECT * FROM test_table ORDER BY id DESC LIMIT 5")
        rows = cursor.fetchall()
        
        print(f"\n✓ Retrieved {len(rows)} record(s) from database:")
        for row in rows:
            print(f"  ID: {row[0]}, Message: {row[1]}, Created: {row[2]}")
        
        # Get database info
        cursor.execute("SELECT COUNT(*) FROM test_table")
        count = cursor.fetchone()[0]
        print(f"\n✓ Total records in test_table: {count}")
        
        # Close connection
        conn.close()
        print("\n✓ Connection closed successfully")
        
        print("\n" + "=" * 50)
        print("DATABASE TEST PASSED ✓")
        print("=" * 50)
        return True
        
    except sqlite3.Error as e:
        print(f"\n✗ Database error: {e}")
        print("\nDATABASE TEST FAILED ✗")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        print("\nDATABASE TEST FAILED ✗")
        return False


def main():
    """Main function to run database tests"""
    success = test_sqlite_connection()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
