# Apache Airflow Playground
Apache Airflow application to get started

## Dataset
CSV file that contains data from the Google Play Store. This dataset contains all the information about the mobile applications registered in the Google Play Store.
**Columns**
- App - Application name
- Category - Category the app belongs to
- Rating - Overall user rating of the app
- Reviews - Number of user reviews for the app
- Size - Size of the app
- Installs - Number of user downloads/installs for the app
- Type - Paid or Free
- Price - Price of the app
- Content Rating - Age group the app is targeted at - Children / Mature 21+ / Adult
- Genres - An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.
- Last Updated - Date when the app was last updated on Play Store
- Current Ver - Current version of the app available on Play Store
- Android Ver - Min required Android version

## Expected Pipeline
1. Read the data from the CSV file
2. Filter applications from the dataset with Rating greater or equal to 4.0
3. Write the filtered dataset in a new CSV file

## Second Exercise - Hive/HDFS
## Dataset
Table in HDFS that contains data from Kafka topic usage. This dataset contains monitoring information about each topic.

## Expected Pipeline
1. Read the data from the table
2. Count how many entries each topic has
3. Write the result in a new table in the same schema
