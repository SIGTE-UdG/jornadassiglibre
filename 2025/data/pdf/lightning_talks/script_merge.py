from PyPDF2 import PdfMerger

pdfs = [
    "2_presentacion_JSL_JVL_2025.pdf",
    "6_sig_corporativo_junta_andalucia.pdf", 
    "7_spai_chat.pdf",
    "9_estimacion_humedad.pdf",
    "11_overture_maps.pdf",
    "12_sensores_remotos.pdf",
    "13_ecosistema_europeo.pdf",
    "14_presentacion_Geomatico.pdf",
    "16_geoinquietos_lightningtalk.pdf"
]
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("resultat.pdf")
merger.close()
