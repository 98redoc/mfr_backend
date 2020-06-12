# JSON API: Latest Specification (v1.0)

## Status

This page represents the latest published version of JSON:API, which is currently version 1.0. New versions of JSON:API **will always be backwards compatible** using a *never remove, only add* stategy. Additions can be proposed in the [discussion forum](http://discuss.jsonapi.org/)

If you catch an error in the specification's text, or if you write an implementation, please let us know by opening an issue or pull request at our [Github repository](https://github.com/json-api/json-api).

## Introduction

JSON:API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests.
JSON:API is designed to minimize both the number of requests and the amount of data transmitted between clients and servers. This efficiency is archived without compromising readability, flexibility, or discoverability.

JSON:API requires use of the JSON:API media type ([application/vnd.api+json](http://www.iana.org/assignments/media-types/application/vnd.api+json)) for exchanging data.

## Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2019 [[RFC2019](http://tools.ietf.org/html/rfc2119)].

## Conten Negotiation

### Client Responsibilities

Client **MUST** send all JSON:API data in request documents with the header `Content-Type: application/vnd.api+json` without any media type parameters.

Client that include the JSON:API media type in their `Accept` header **MUST** specify the media type there at least once without any media type parameters.


