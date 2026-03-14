FROM node:20-alpine
WORKDIR /app
COPY package.json ./
RUN corepack enable && corepack prepare pnpm@latest --activate && pnpm install
COPY . .
CMD ["pnpm", "dev", "--hostname", "0.0.0.0", "--port", "3000"]
