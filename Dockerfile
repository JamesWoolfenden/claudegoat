# CASE: mutable base-image tag — no @sha256 digest pin
FROM node:18

COPY src/ /app/
CMD ["node", "/app/index.js"]
