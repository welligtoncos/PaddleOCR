from paddleocr import PaddleOCR

# Inicialize para português (ou inglês se quiser)
ocr = PaddleOCR(use_angle_cls=True, lang='pt')
print('✅ PaddleOCR importado e inicializado!')