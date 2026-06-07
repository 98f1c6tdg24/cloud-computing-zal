#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

cd "$ROOT_DIR/lab03-terraform"
terraform destroy -auto-approve

echo "Infrastruktura została usunięta."
