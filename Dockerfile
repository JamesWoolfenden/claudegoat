# CASE: mutable base-image tag — no @sha256 digest pin
FROM node:18 # ghat:suppress - test data: deliberately unpinned

COPY src/ /app/
CMD ["node", "/app/index.js"]
