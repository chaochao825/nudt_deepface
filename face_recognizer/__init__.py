__all__ = []

try:
    from .deepface_model import DeepFaceModel

    __all__.append("DeepFaceModel")
except Exception:
    DeepFaceModel = None
