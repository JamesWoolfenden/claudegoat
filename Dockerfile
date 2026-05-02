# CASE: mutable base-image tag — no @sha256 digest pin
FROM node:18@sha256:c6ae79e38498325db67193d391e6ec1d224d96c693a8a4d943498556716d3783 # 18

COPY src/ /app/
CMD ["node", "/app/index.js"]
