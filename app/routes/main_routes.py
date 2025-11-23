from flask import Blueprint

bp = Blueprint("main", __name__)

@bp.route("/healthz")
def health():
    return "ok"
