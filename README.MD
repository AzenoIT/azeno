# Azeno

## Monorepo

### Add new dependency
1. Make sure package is copied to docker image.
2. Install package as workspace dependency `npm i ./path/to/package/folder -w workspace`
3. Install all other dependencies `npm i -w workspace`
