from dagster import asset, Definitions

@asset
def my_asset():
	...

defs = Definitions(assets=[my_asset])