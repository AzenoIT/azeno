# Azeno

## Monorepo

### Bank

1. Internal imports should be absolute `import X from "@azeno/bank/..."`, for
   example `import Button from "@azeno/bank/components"`.
2. File structure should follow convention of grouping
   by [route / responsibility](https://alexkondov.com/tao-of-react/#application-structure).
3. 

### Add new local dependency

1. Make sure package is copied to docker image.
2. Install package as workspace dependency `npm i ./path/to/package/folder -w workspace`
3. Install all other dependencies `npm i -w workspace`
4. Add compiler option path to properly resolve imports.
