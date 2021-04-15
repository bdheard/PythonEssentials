---
title: Lesson 12
subtitle: Python Essentials
---

## Overview

1. Working with JSON
1. Working with XMLA
1. Working with HTML

## Working with JSON

- JavaScript Object Notation.
- JSON is built on two structures:
  - Collections of key/value pairs.
  - lists of values.
- Python json module helps you encode and decode JSON/

**Key value:** "key":"value"

```json
"userName": "John Doe", 
```

**Sub keys:** {"key":{"subkey0":"subvalue0","subkey1":"subvalue1", …}

```json
"userName":
{"firstName": "John",
 "lastName": "Doe", 
 "prefex": "MR"},
```

**List:** {"key":[listvalue0, listvalue1, listvalue2, …]}

```json
{"tags": ["bear", "polar", "animal", "mammal"] 
```

:::notes
JSON Linters will format JSON so it easier to read by a human. The following website have JSON linters:

JSONLint
ConvertJson.com
JSON schema linter
:::

## Retriving JSON data

- **Key value:** 

```json
"userName": "John Doe" 
```

```python
print(results['userName'])
```

- **Sub keys:** 

```json
"userName":
{"firstName": "John",
 "lastName": "Doe", 
 "prefex": "MR"},
```

```python
print(results['userName']['lastName'])
```

- **List:** 

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