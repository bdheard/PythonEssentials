---
title: Python Essentials
---

# Module 12

## Overview

1. Working with JSON
1. Working with XML
1. Working with HTML

:::notes
:::

## Working with JSON

- JavaScript Object Notation.
- JSON is built on two structures:
  - Collections of key/value pairs.
  - lists of values.
- json module 

::: notes
:::

## Working with JSON

- **Key value:** 
  - "key":"value"
- **Sub keys:** 
  - {"key":{"subkey0":"subvalue0","subkey1":"subvalue1", …}
- **List:** {"key":[listvalue0, listvalue1, listvalue2, …]}

```json
"userName": "John Doe", 
```
```json
"userName":
{"firstName": "John",
 "lastName": "Doe", 
 "prefex": "MR"},
```
```json
{"tags": ["bear", "polar", "animal", "mammal"] 
```

:::notes
Notes:

JSON Linters will format JSON so it easier to read by a human. The following website have JSON linters:
- JSONLint
- ConvertJson.com
- JSON schema linter

:::

## Retrieving JSON data

- **Key value:** 
  - "key":"value"

```json
"userName": "John Doe" 
```

```python
print(results['userName'])
```

:::notes

:::

## Retrieving JSON data

- **Sub keys:** 
  - {"key":{"subkey0":"subvalue0","subkey1":"subvalue1", …}

```json
"userName":
{"firstName": "John",
 "lastName": "Doe", 
 "prefex": "MR"},
```

```python
print(results['userName']['lastName'])
```

:::notes

:::

## Retrieving JSON data

- **List:**
 {"key":[listvalue0, listvalue1, listvalue2, …]}

```json
{"tags": ["bear", "polar", "animal", "mammal"] 
```

```python
print(results['description']['tags'][0])
```

:::notes

Output:
- John Doe
- Doe
- bear

:::