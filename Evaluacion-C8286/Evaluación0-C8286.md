La Shell de Linux es un intérprete de comandos que permite al usuario interactuar con el sistema operativo mediante la ejecución de comandos. Actúa como una interfaz entre el usuario y el sistema operativo.

![](https://lh7-us.googleusercontent.com/k_LnWfHp8hHcVuNDM6EhG72PPFSbElT-wvInnsWO0Qni2EfBvnBES_mioZMF62fpakc9ZJYqnFPsQC2NaQR7FQ5LzK1szPPbeT29LVwJ0cHQTz0CJyeaSsVmk__uWrdarMaShAQdoPbEgmS1XDiuvH8)

## Sección 2: Navegación

![](https://lh7-us.googleusercontent.com/l6jCsKM2g7eBbgFT1urFABbxvAbRLZu5bImTdLKwG3u00gRcaX5uSADpAELvcy69-1JWZbSmZYA32Y9CTbYfEZqABPxWwD3aKPjb8CNnxnmzPj5BqW0-i64dsCCgFy5ydhj4-6HoTtGTkd17YiqVGo4)

## Sección 3: Explorando el Sistema

  

![](https://lh7-us.googleusercontent.com/1hL1xC2z_fuq8yZreFCfoL1lqMfTOs-zTSjpqV7hJEtgYZwpv1qydngTXSIeGEq6OXYrD1sLWXS6QWEOAUfn9jtwiLQvklzuPwdtqnZspVPr3WWDMN-pIevYYkOZz7_tCp1btnYe3ozZg_4gB569UPQ)

“ls-la” Lista todos los archivos y directorios, incluidos los ocultos

  
![](https://lh7-us.googleusercontent.com/QBOF5CZhprWLFnR2UUXwx1TnSFwPBoJVRA6PV7-QCaxMxeq9cNGUVqGC7SD2K2r4TPgtkyZ3Ed2FZ43rIqMtF947usD5ra6mFyHZ-pcuwWd2_h5Cv23tg4Q08WlP6ujDsx2prufjET0vbrU_AcghF74)

“du -sh *” Muestra el uso del disco del directorio actual y sus subdirectorios

![](https://lh7-us.googleusercontent.com/pJdrR7jDDXwTJpB5bMf1dmytjCLoz_4aNrQUeRqIouS1QFB7DNPTf-Tgz9nhhiUw0KuMUL7_E8xxig7e8Mlt4U9n3av1CwIcNw9UE-sfBmIlzX3Kd4oNENXq1NzRfrQyvTHEuysN8i8nRDr6u94261s)

“df -h” muestra el espacio disponible en todos los sistemas de archivos montados

  

![](https://lh7-us.googleusercontent.com/VXePhdabXkUIoYzNUnNzG1Gx4V4995F2_pPYknsebex2rXnEva7tYHqhijHUbWbHM_-AjVOyd12yNGmQZXtGqTEExo6nZCgute-3coS6APlK9ZwDNnc77GochqoMD9E_XX0-abXqaibYF7OiBwunKFk)

“top” Iniciar el monitor de procesos en tiempo real

  

![](https://lh7-us.googleusercontent.com/3fNhgg4P-yIETeX_Tp4YL6X7yxeJTVk1nvjAdZ3D63RgtM8aW6aYdH-ikguCpHwggp2qOoI6qvufLOLN67WSiNoHIPIPmPML_iwIt2rXCF4hXlHWFZOFAf-XRTCX-BNIRB48xzzImYHPSSFlmgvzInQ)

“free -h” Muestra información sobre el uso de memoria en el sistema

![](https://lh7-us.googleusercontent.com/829SX_82m8VbrY4T7DyFj1pVNlT-tCMgGUH8d0ggqX_Fn8r6WdZN_uq19GDZSIL0OzDXKV2FTgcyUCwQPSD-dfqM00tSNUtcTPqcXQfDHrwzs9RgZqkSHfA_dqPmaVifb8IsfKO3Cg1osEPxuyuIoqE)

“uname -a” Muestra información sobre el sistema

![](https://lh7-us.googleusercontent.com/JwTFT6m309T8w1fN7QxoBgQfa_6zHmB5euyA_DaAwajcGkp1xoeFZo2f4-yhgOZKxDbc_2tqjoyXzkI9zi5zsODZwo8O7fbUGEsLm_AJ_Qn8Y07tOhHSZaLr6STjUxFg2asM0tvf_6W4qas42z9haEc)

cat ejemplo.txt

Función: Muestra el contenido de un archivo en la terminal.

Al ejecutar cat ejemplo.txt, se muestra en la terminal el contenido del archivo llamado ejemplo.txt. En este caso, el archivo contiene la frase "Este es el contenido del archivo ejemplo.txt."

  
  

find . -name "ejemplo.txt" “ find” Busca archivos y directorios dentro de una jerarquía de directorios. Al ejecutar find . -name "ejemplo.txt", se busca en el directorio actual (.) y todos sus subdirectorios, un archivo cuyo nombre sea exactamente "ejemplo.txt". El comando encuentra el archivo y muestra su ruta relativa desde el directorio en el que se ejecutó el comando, en este caso, se muestra. /ejemplo.txt, indicando que el archivo se encuentra en el directorio actual.

  

file ejemplo.txt, se analiza el archivo ejemplo.txt para determinar su tipo. El comando devuelve ejemplo.txt: ASCII text, lo que significa que el archivo es un texto en formato ASCII

  

## Sección 4: Manipulación de Archivos y Directorios

  

![](https://lh7-us.googleusercontent.com/BFHbRFpSvmU_gAuogtceDsZAmkALq-eXQzQeQbG2GpZL6jSioYABRcdLoJwrzCPr5vMaanQ3h_MLkrTwERTTUm9Hoe0XDnXINvKKK4Q3d6FIBAzWC40OTux2oPHbsufwr-Orc7TAA5qNIGPg4iz-MyQ)

mkdir Proyectos: Crea un nuevo directorio llamado "Proyectos"

touch Proyectos/nuevoArchivo.txt: Crea un archivo vacío llamado "nuevoArchivo.txt" dentro del directorio "Proyectos".

  

“mv Proyectos/nuevoArchivo.txt “ Proyectos/archivoRenombrado.txt: Cambia el nombre del archivo "nuevoArchivo.txt" a "archivoRenombrado.txt" dentro del mismo directorio "Proyectos".

  

cp Proyectos/archivoRenombrado.txt Proyectos/copiaArchivo.txt: Crea una copia exacta del archivo "archivoRenombrado.txt" y la llama "copiaArchivo.txt", dentro del mismo directorio "Proyectos".

  

rm Proyectos/copiaArchivo.txt: Elimina el archivo "copiaArchivo.txt"

  

## Sección 5: Redirección

![](https://lh7-us.googleusercontent.com/35JYGdBRl1melv5D4FI2xJip7HwfCgjwGceyA40WdNWiSplIQVvItwEzWvqjDUqEMaq1E6gt44YyVsjyVPqrzW86ovfLHeyBKmLMX6uhLs6AskEIYUcVNkFkn_APKfkqcVhDn9cab5zbZnhkeMt-IDk)

“cp file1 file2” Copia un solo archivo a otro archivo

“p file1 file2 file3 directory” Copia múltiples archivos a un directorio

![](https://lh7-us.googleusercontent.com/Kh5L28j_pQfuoNGArX1zBwg1jOGwVvaJSn31J6e-8vOZ-UctSB5lsVOKe8ibKoulYTSus3rIRd0EeV3drmP4UshmE70ENWeDSNMN3mHEXNS1h158Bu1Uid5Oe2ngMOTF0fvNeNEOSfyG-leWW9aSlV0)

“cp -i file1 file2” Copiar archivos utilizando el modo interactivo

  
  

![](https://lh7-us.googleusercontent.com/bulrzfTYSLxfKm6HeLx4zfrb_4JLqTkmMPrDBtIrT5T_KzpEayDafksg9sl0YPc7zINDxDXXbDOY1KwFq6vgnd8CBEq28aciqF0hb4-ALKYFvs2ltH0SzsNcLCdB8p0OCtNBIQRF6OYgVxSOkgqShMU)

“cp -R dir1 dir2” Copiar directorios de forma recursiva

  

![](https://lh7-us.googleusercontent.com/epLpuiL10dSBR6z4lqRwkOY0fkq18Yh5YZ3qsyn8IHP4rkUf3ndGSKurzIakdzOIHY5_lx1ZI--tTfnIfnnwW8Z7I5lB8IYJ8FXBmNtaNtpNZPvI4L2n8C_MRJHY6DuYCi52VBjER_aS_FqRIT0c8m4)

“mv filename1 filename2” Renombrar un archivo

“mv file1 file2 directory” Mover archivos a un directorio

“mv -i file1 file2” Mover archivos con confirmación interactiva

  

![](https://lh7-us.googleusercontent.com/JxpYWft66093EmZ6cLo85QkkiOtrpayimqm1tQdJdVNUSNSuygFPybRb8IXgP6ZoHYFJo7toIWPzNi9K-Ez-V2utrDNXK_cXFoFWMYUgxNafrS2ydV8dXR06MZ7qrwA0rhn0IqtESIe8wfud004zOUI)

eliminado archivos y directorios

“mv -i file1 file2”

“rm -r dir1 dir2” Eliminar directorios y su contenido de forma recursiva

  

## Sección 6: Ver el Mundo como el Shell

![](https://lh7-us.googleusercontent.com/6ATNFqPIKbtY1xVUBt-j7j_oVw3GGxoO87B9mSZ1pvC0QuZkMiMhkLtew-XyejXuensSNAR8mRN9UyY1PZT5Hlhkdf_W8dOUi6h9AHJGI4OJfQ70hhRXHpk48T4KZ8YMlvSQ4UG09E3ZpEeiv_u_6pM)

“type ls ,type cd” Muestra el tipo de comando (programa ejecutable, builtin, función de shell) que el shell ejecutará.

“which ls” Localiza la ruta de un comando, mostrando su ubicación completa si es un programa ejecutable.

“help cd” Muestra la página de referencia de un comando interno (builtin) de Bash.

  

![](https://lh7-us.googleusercontent.com/p6DGj_Oy1kB-WJajVNLJdl92jFEwLBWVNrQkH3MtlHWI_W_Kq0qVZk44uLCo_CanLBTT4_DKQmCfJHII6Jmcd2j7d1Dbz9D9NVCMBL_XBT7XhLVhQPQlP1P-NEx4K_2exKhhHSSyVsD8yBFzg0eGgEM)

“man ls” abre la página del manual para el comando ls, mostrándote todas sus opciones y ejemplos de cómo usarlo.

![](https://lh7-us.googleusercontent.com/P6bvxLL102Ydbv3qIwlagKC57ikezkb8rHIQ_yrbjcmiHAJEvRTmyMzo9J2l6Op5N9NLslzranevJxpeBWVu_jUoavs_cYtx36Q0gu9bBtC12Xh4Ks6RJw0UCh3nGP_qXnP1UXcE1yLcv7vpvOOlRJQ)

echo El usuario actual es $USER: Imprime el nombre del usuario actual, que es "oviedo".

cho "El directorio actual es $(pwd)": Muestra la ruta del directorio actual, /home/oviedo, usando el resultado del comando pwd.

  

7.-I/O Redirection

![](https://lh7-us.googleusercontent.com/91yqr9HN90wFZILZIpvgQQg152iSX1yPYW4J0CBi9XczQaH2ltmibBAdhBLi0XKn3qoNFYCaI201NBU7XbR8ulOK1mTiHDvm34OWLEu8-HzV1kph1ycAtNRU52wjKE0jiNDLQg-H39r3zuRnoClze-g)

ls > file_list.txt: Lista los archivos y directorios en el directorio actual y redirige la salida al archivo file_list.txt, sobrescribiéndolo si ya existe.

ls >> file_list.txt: Similar al anterior, pero añade la salida al final del archivo file_list.txt sin sobrescribirlo.

sort < file_list.txt: Ordena las líneas del archivo file_list.txt y muestra el resultado en la salida estándar

![](https://lh7-us.googleusercontent.com/J5UdnsJ60gqBJeHHKItcb5VCZmUCrT_NpSg7861F6GjjnC70is6XFDYkXIp59fsk3KE4E3Pmie1UkEd-121v9qhPpaKAfEo8uew3XJg6XEMpE4zjqbRMaiHOxRibsENsPASNjG_1YeMSCEmtjygN-IY)

ls -l | less: Muestra la salida del comando ls -l en less, permitiendo desplazarse por la lista de archivos y directorios

![](https://lh7-us.googleusercontent.com/g9rZjW_qlnkn8xSfDu5AUOoWvxpOUCOs2cusSQFe_hlPpTi2TobAojWWEaxZLsaHKWmjcmIU_hNK3Y7vewOsgZmiKB70fVrDtSLtd1S_e2njNm8uh5r3R6HyM9Rzpz_8hGm0XIfJ1V4kb3-7YnD8gqc)

ls -lt | head: Muestra los 10 archivos más recientes del directorio actual

![](https://lh7-us.googleusercontent.com/-ica_pCJ3lvbTOR2gLwhEHaf5lVacLHbRAlQTR-5Xxvb_PKyI_0B32kZB-1JdwLTOdbAK7TKwR7gwkjoAIUpvfDMPA2Wcgntgz-sa2n__kOEYl0VkLYRotlLx3tN-xvEWebtgZ3NVP1RTCtIaRLOFuE)

du | sort -nr: Muestra una lista de directorios y el espacio que consumen, ordenada de mayor a menor

![](https://lh7-us.googleusercontent.com/jiHHA_FvaE26sBHyrX_LRWOUfehea6oP7s5QUgFwYv7h9BGtu7110jn3Dd3nYl51f9vCaAf67Vp2TGzjOpvi67Hs2Ro0_B8IbylmDgbF9VaUNgIr4-oUkJb__BG3hqkzJpoyrUNtn5ghQg0F1iL_dBE)

find . -type f -print | wc -l: Cuenta el total de archivos en el directorio actual y todos sus subdirectorios.

7.Expansión

![](https://lh7-us.googleusercontent.com/dpqBUkXzKQUaYfcuKPgpsGmZSz_voLtu_zlpiJ-kacWzrXsGEW27tKZDTTXnNf_eQc7WS6hTYRJvMEWixqYBs6p_45DyRG0Qxlf4Zru-yYmZrsA5VyQ1gKYgHhufWh_fyQB--e5CCKcdhWTOIQWdWDU)

![](https://lh7-us.googleusercontent.com/VvXZYd7nk2DvCJa7MuAKVvX5GXoe_bVejKy5lnaEjlMwappdPZ-nLcdmM2P9v_bp2UoIvZDE-1zabg-9a3K_Qii9qUmmy9Ry0JTtQn4-hVYA5bEsHQYWMWPqRGX58Qei2_cMdb1XQBqnUjfuU7pK9SQ)

![](https://lh7-us.googleusercontent.com/YHkQZpxJvtBHl61qj6hWEt3OtmSVsob9ju70-hHm8f9_BjjYkfORatifdHP-FmDRaqGAK-kvlg6CA12GqW2yplC-mFAGkUoB-BBHGDyylfCPr9MaTi1mzqS1pRhcSqzJZYDtC1xbe8PX_4Dy-1sYspY)

![](https://lh7-us.googleusercontent.com/EyfqfM0tnmV2p-BtiQeN9oWhFznQb_-AtMwzkS95uTg7yYltTxfE3I6f7vrL-raeDHuZJgEnBQb-Pc-d6xxh27MO2Zn6F3EL-u9UvJADRt5YGJGtGP98HozlBkr2j2jgBH_aKYDKweRiQIvsHYMl4J8)

![](https://lh7-us.googleusercontent.com/UYZ_5KMU6FID5-qLlyRz1IS1GyW8mN78XB9PEs7Q6AMV9zK7Vga9_FYgT2PJ1RK2_C5T0DxPgWmu9_GaG4vF6XwffpnlPt3yFs_bPBuNErejXVmlBy96QC7RGHjnZ3fdZqtzOE8yBpqIrFreKv3_L3k)

![](https://lh7-us.googleusercontent.com/SmxDSgCRSeB-loAszgoiKQFmh3cqJdguzoZmfRKfDmWLQbnEYTRMS8oRF2kUq7TsqrH7FZ8fxbRrA1X94y_fVEqd7cQog-wl6YTvfoLD9FJ4duGh5YH0AuoX0bb2qqae5XRqA9N2ku0YxiY31INFGLc)

# 9.-Permissions

1.  chmod - Modificar los derechos de acceso a archivos.
    
2.  su - Convertirse temporalmente en el superusuario.
    
3.  sudo - Convertirse temporalmente en el superusuario.
    
4.  chown - Cambiar la propiedad de un archivo.
    
5.  chgrp - Cambiar la propiedad de grupo de un archivo.
    

![](https://lh7-us.googleusercontent.com/Y6t3bELnL4giGPPRjVDynoNfYzD8UVwM4-4DIGGw3DKbFIp9VJdDFRM1mntRtA_eZBLttXVwKHn-4aEh2Hgnp8qqqrs3GgW7bN6eHLoOBwpX9J92CpvkNAHvA-r6Kca7DzIAHde45UTaa6hfmEsIv-M)

![](https://lh7-us.googleusercontent.com/9I5KeQjpDdSncmVtOYw61eHdFPc_pNnU0R05nzD1eV0Ih7pD7kFVovO9Fn-f3e73cUlH_ZOUckA09drG9Rm1sFCC96DxPiZ_5oMWrfq8Ykb9t0-QwEnmyy57433BICJHGJBQ-OGuPuHw0-6qAV73Ao0)

  

# 10 Job Control

![](https://lh7-us.googleusercontent.com/3bbvMBxRADV7MvRFYOadSZ4_DePrtVabKaiZ1S_YwkjJZ417HFii_U0QN6zSkQE7eWi6aPKSDiC4_NDt-3aiqGgQD0c9jRdqtnLMI0dAtZ5JJnPMsikCQHHSWX76YIQe-sGOaOVoAfa_-cK-rABSPB8)

![](https://lh7-us.googleusercontent.com/4blHw2vpeHDUybCfNL3Nc2ihHUXbCc9Jbo7nqsZlH79mpzlLzjAKf3cthI1ihyAIRjD-NL7_9NnHMyS6PHhbh-GWYMCaO0w3ilCQhINfcLF5xg8XOPOc6-jD3TE1HPMLbyWBTEOoIU2E7swIxC13Moc)

![](https://lh7-us.googleusercontent.com/H74weTKdEL3-6a-Oj9X9cd6YKoWOSrc-lEC87Ya2rA5NwYg-K8GlCfrT2tGp43SUvtRipkKkTFURlQvjmcl_Rm4WQL-1sLG5WesqS0i7nv59jl9vUlK5b5W9i8706W7r97EhQxrnqnldq7e4BAGrkSc)

![](https://lh7-us.googleusercontent.com/iA6jXGBqnXlv8rCwGQ6qTNKsBpmI1k_yc6BpJNwXj0mxMHVIsIQgECC1R6AB48I-aI4GyzZwFoGL2WXl2Am7kWwrZtQLyw1r3IAdk6fSluncpRP_RHsj6zgVH0htg5Wse1YXllKGCcEcoJlMNAsXPJ0)

![](https://lh7-us.googleusercontent.com/XtpIx5_bkz7e4HDn-CqLM32PcqC1MyB01Myq3P-M1DsfXns1lrRnoPSURXP2e3gKaPSJjRCv7DQNU2F7zL4xXImPO0WTin0Uu3yKN2TOvajGtPdYnYNDj1J3Y1PYN2u-ybR9cKZecFXqnN_VBZ2vUa0)

![](https://lh7-us.googleusercontent.com/yzakcHM-rHLjn_BjAydu1FuqfbLq-ISxHenqbgrdyiUwuipDtMbycV2qFaKxOvWhefuaJImraQA5v51CheFqrdGjlu2antKy-oXTl2mLLbhPW_MQhUUEU30fuUHNdNdeqBgwYRblBEJYmR27sam8eCs)




