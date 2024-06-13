
Monitoreo de procesos por uso excesivo de CPU

![](https://lh7-us.googleusercontent.com/yJkPda8FZ3lByVjWhVvvB6Vx2mnnEIs0Zf1-3uEbe_oDt1N2-HzC1NFbDpVHI-qS9b6Gj-6uwn0kvpCVJ0eQQoSebjsMoQmmamt8xr3Q93TiBO_Swv9Ifzh-DNDOHQ9Ben6FTeGRWwaFFKYfAV5XE7s)![](https://lh7-us.googleusercontent.com/Aiyn3lZ_whFAqyqxxVY2k1WXEz4FWc5dMgQM3t4UFcFElygyfgEGGkofs2ymBLBepJcXrsNQeanmQvW_pimUYKRuZuMG64f5Ye_d7X3MQCiCSSmJyDKGb6ddor2tmTL44nkzTIKbzSAw3NFzdPLBU3o)

Comando ps: Ejecuta el comando ps -eo pid,%cpu,cmd --sort=-%cpu lista todos los procesos activos, mostrando el ID del proceso (pid), el porcentaje de uso de la CPU (%cpu), y el comando que inició el proceso (cmd).

head -10, que limita la salida a los 10 procesos que más CPU están utilizando.

Bucle while read: El bucle lee cada línea de la salida del comando head -10 (que a su vez viene de ps), asignando los valores a las variables pid, cpu, y cmd para el ID del proceso, el porcentaje de CPU.

Uso de awk para filtrado: Para cada proceso, se pasa el porcentaje de uso de CPU a awk mediante echo $cpu | awk .... Dentro de awk, se compara el porcentaje de uso de CPU (cpu) con el umbral de 80.0%. Si el uso de CPU es mayor que 80.0%, awk imprime un mensaje indicando el ID del proceso, el comando, y el porcentaje de uso de CPU.

Las variables pid y cmd se pasan a awk mediante -v para ser utilizadas en el mensaje impreso.

El código dentro de {if (cpu > 80.0) print ...;} se realiza la comparación y se decide si imprimir el mensaje.

### Ejecución

al ejecutar el script con ./monitoreo_cpu.sh, este realiza todos los pasos mencionados. el resultado indica que el proceso con ID 1978, iniciado por el comando /usr/lib/firefox-esr/firefox-esr, está utilizando un 89.0% de la CPU, lo cual supera el umbral del 80%.

Identificar procesos zombis y reportar

![](https://lh7-us.googleusercontent.com/iG_8X1kiHvH4cncHzTLf3jY250YsPWZoP-Gy6zypCxvimjptYzHSCcxGEL1LvikEYRJUnWkFXhAEe6tMzYKBhbsv-r7QTOQ-43Yh0GC7fdW0lR4u4ZI1ROHAa8gPV4Lss5jN0GkOHpkN26V82HCiH8w)

  
  
  
  
  

Reiniciar automáticamente un servicio no está corriendo

  

![](https://lh7-us.googleusercontent.com/d-bY6W8wx0izluWMNIvJEQnUu6OLyL9sfFEKqTS8-OEz6sXcsWUOcQyZk-sgzQY1zKbHZOSPkXD6vqNIdaLhwJFWMuMCC3MxgnfxItYajlaVCezDuKuHdCe9tSUpTsySZAf5ZX1PONxW-m94d28jbPA)![](https://lh7-us.googleusercontent.com/Re8O6ur4qF6YbjnzEc3i0ls_WfbV_VHcwMsbDLFQqbBLdNcEoohqk1NXvQjWHgI3mw59wlnfcc7uW4klrrTyfTfMXs73Yj8T0guZWGcfssqWVKi0aYCECBJjjGayu2FRmKMZhTPfxQtKeRzSEfAjGrc)

  
  

Verificar la cantidad de instancias de un proceso y actuar si supera un umbral

  

![](https://lh7-us.googleusercontent.com/iB_IE9Xpa6HpDfpnON83WaQYck2pOmzkXiqWM-29QhkOSvCj18f0kQ8Q6-eU03U0jvYkabirZttkPjVgjKSPyeIPcfKSPMHQoxHmPBL0l6MtArFyJrK6SgnrXyZn0SHF5lPgZ1dxF4xVBnr7GZp4twU)

![](https://lh7-us.googleusercontent.com/yCxAcTJWyOzvz5g_IZZAGe1c14X5L484st0rHTFRmMIBYBiOccRFFoKv56qHxC86yK3twIkjeLPAPMuhX_l9eEFN6kbMBqEDD91-z8Hvx1GfECKLOncx3r_u2Q_Qhj47jpVuCv3fX0i1k3vXzy9qvL8)

El script instancia_proceso.sh realiza las siguientes acciones:

Define el nombre del proceso a monitorear como "httpd".

Establece un máximo de instancias permitidas para ese proceso en 10.

Cuenta cuántas instancias del proceso httpd están actualmente ejecutándose en el sistema.

Si el número de instancias supera el máximo permitido (10 en este caso), imprime un mensaje de alerta indicando que se ha superado el número máximo de instancias permitidas en este caso el resultado no me imprime nada x que no superó

Listar todos los procesos de usuarios sin privilegios (UID > 1000)

![](https://lh7-us.googleusercontent.com/80ZE_LsVeWg7P3xtbeE82_kApb1Dp4rFn53up_XDjiY9w30QyC-Kqm2GpvnI4SivaKeN7PI8DvAMejYsduLTmQTIsWV5eNv50o0cMnQVkjUlaqhvILmulvK4PN5Ije5Tmjn8m6dfkFwLmEO8fpMkTlM)

![](https://lh7-us.googleusercontent.com/0rQPJE0EVyahkVh5DFCB1M3d8-G85UzcpRKyjdn4FwC-yPbtjuhvVv__B8PBzccqZG34MfkCE1u9Mia4iCDymJ5C6-jcgWkxz8UsbF7HURswn8Zrh2U3VbbeCsRJwCuEsCLI0ezo5M4ScWzCVGC7SPw)

El script usuario_privilegio.sh realiza las siguientes acciones:

Ejecuta el comando ps con las opciones -eo uid,pid,cmd para listar todos los procesos en ejecución en el sistema, mostrando el UID del usuario, el PID del proceso y el comando que inició el proceso.

Utiliza awk para filtrar y mostrar solo aquellos procesos cuyo UID del usuario sea mayor a 1000, lo que generalmente excluye los procesos del sistema y se centra en los procesos iniciados por usuarios normales, no privilegiados.

El resultado mostrado tras ejecutar el script indica que se imprimió la cabecera de las columnas (UID PID CMD) pero no hubo ningún proceso listado después

  

Alertar sobre procesos que han estado corriendo durante más de X horas

![](https://lh7-us.googleusercontent.com/9JsxpK7j9fw-sYDm1_TV3ZiWm6VEr6nyQkkPsbAjS0V2CYFGNp5B5GUpPmpKwqUP5qXTFf2pqfzJaTk9FjtmgWFBTUOVSs_BkfXSDQ4DP0LSp1izUE0AMPD-hHuja-0JoaqRTLl9KKTWwO5gECIDJRo)

![](https://lh7-us.googleusercontent.com/PYXt7fqdWqw9zUZj8P7GMH2xUr0hH2NC7Z11XFx_LOd5dA19najx-k5NLH_vfSewMPJ9p_3xlsWi03hlrkFL-LU31rzp2mHjujPbVQYNpMxXQe9kYt704E2mzPhaAI0N_erpvEl314QXOaDuvYjxjd8)

La ejecución de tu script proceso_xhoras.sh indica que ha encontrado varios procesos (con PID 1, 2, 3, 4, 6, 8, y 9) que han estado corriendo por más de 24 horas en tu sistema.

  

Encontrar y listar todos los procesos que escuchan en un puerto específico

![](https://lh7-us.googleusercontent.com/rKqkC4m-GK1aM0EK7cPIQQ_1q28WTQsP7TaONbClE1syxCJkYWd10MP87NkYoI4u3PUmGKpsAHaCFyuzSUtIX6r5TVgMt8JgSulcT4iA37iGcyi3d4L91_b5XkZx6jerEFqS67ZJva7YT5Ej7dWj4H8)

![](https://lh7-us.googleusercontent.com/EhOpDuZVj0TDBiXkEykLYB1aTVjp0z-etgU43ay6MWeL1zg2IHniGvhp3JYLWIjxjtgkeglMqSX75ybcf76YJ_pm2zitRlzBrDXfMAEtSkBL_VZiSfjc5fVt_xnA1nomwjVkzHyBABxR1981WZ0fC8E)

![](https://lh7-us.googleusercontent.com/gZNcYdcFgPTnOYXoHgYWiA_tn_W13AoX96OexApM1yVeG0TSkzAkxFNA1lO1rdWX-n2VNCTr1DDdueumpDmUFGkwao9lB6tTUV-C0TOHHCU667Y0xnt8c-bVdgoSdCfM47Uh5uO_9p-8xqr7tFQVM6E)

La ejecución del script puerto_especifico.sh busca identificar y mostrar información ![](https://lh7-us.googleusercontent.com/zOVErGJMEFhnhidWP4Oo7CQP3eQSD0ZAPmqWpU6CXxRXNGZo0kcZ1v8GpVL2JmcN_Y9a3zUMaowdXbrxghR7wc9GHmNz0O17QEEaN6Mhl8nanQSTCATwlAIItEGR_Sg0TAeALYXUleUlz7K7kkj0NUg)de todos los procesos que están escuchando en el puerto 80. Sin embargo, la ausencia de salida indica que, al momento de la ejecución, no había procesos escuchando en ese puerto específico en mi sistema

  

Monitorear la memoria utilizada por un conjunto de procesos y alertar si supera un umbral

![](https://lh7-us.googleusercontent.com/hy75xxVbs2MLJOORNVhZC2TXWGt-__QO4DUfd2Ng_XNbcy50TBYWv0zv8jnW-CoelX4UCINQ7FVHC5tV8vzzzquloPFZW-qohM-08GxrT3rQbm4d-eJQl2KCahHjcQxMzBskhLwY455CtRu_M0gnBY4)

  

![](https://lh7-us.googleusercontent.com/0aupVyqJNq280saZRiY1Comaz3VJQkkz87C8hN-nqvfuxGcyR2bvU9gEli_sN2McM9-BrtoxssEJJrp-tRPsRmzaXUApAWt9iun85He-XLKNUtxRV43HWKzD4E8fPZXIB0TgxbW_I62_Z34Um_QWS2A)

el scrip monitorea la memoria utilizada por los procesos que coincidan con el nombre dado (mysqld en este caso), comparando su uso de memoria con un umbral definido (101 GB, representado por 1024 MB). Si algún proceso supera ese umbral, el script no me imprime nada ya que no supera el umbral de memoria.

  
  

Generar un informe de procesos que incluya PID, tiempo de ejecución y comando

![](https://lh7-us.googleusercontent.com/hGtKamrUy7lEfc3hNfnb6wQi29NDyelXOi_mRw5VjVW5TlJ_Vvuovzxq9iqnV-9C2yIcYJ6tr7WcdWAbZTUg_DRaUgsbEN1lT6k06ee2K299qgaT7rdSyx1ieHEI3PSQM-Yp03PaQ9MLWCt5Ap5wZPI)

![](https://lh7-us.googleusercontent.com/iKVHQWO90t2NICpDrYFSSXhM_Nz1bvTN14T9AnHOTYPiWGY-lHovI4Tk7BXhwFmRIDqQwEnJfk1Cn2j1NjYkRXMgTmIJeUZe3pb-I_8SXIK0iYjMKbq2dPvdrHqcUrqMNJ-2ZH5HvqiDt46aqjICvhY)

el comando ps -eo pid,etime,cmd --sort=-etime lista los procesos actuales en ejecución. Los parámetros utilizados son:

pid: Muestra el ID del proceso.

etime: Muestra el tiempo transcurrido desde que el proceso empezó.

cmd: Muestra el comando con el que se inició el proceso.

--sort=-etime: Ordena los procesos de acuerdo con el tiempo de ejecución, desde el más antiguo al más reciente.

head -20, el script selecciona os 20 procesos que llevan más tiempo en ejecución desde su inicio.

proceso_informe.txt, guardando así esta lista de procesos en el archivo

Al ejecutar el script, se crea un archivo llamado proceso_informe.txt en el directorio desde donde se lanzó el script. Este archivo contiene una lista de los 20 procesos que más tiempo llevan ejecutándose en el sistema, mostrando su ID.

  

El comando grep

Filtrar errores específicos en logs de aplicaciones paralelas:

![](https://lh7-us.googleusercontent.com/-l6Kut0rr3KJZ3oyR_jWWp7zrHhf2cWHTk3fNm0caGzbdhw2z8wkQwrJ2b_8nDLbxvHhAwPRyQKC4pajjtuf5iSDKwbmTZJ_-mw9wE2fN0H6bg8zUxr8PI099D-YsMkbLho7e9diidxCG1lk33fxy9s)

  

Verificar la presencia de un proceso en múltiples nodos:

![](https://lh7-us.googleusercontent.com/9a32yTKvLGRfB7Fb_wQeV14OM2XlwahROoWVwD3e5wxrN_YM7kk4B4b2i9R8vsZutRdz59rFJlOVqTnYcmhZdvjiwVQq7H1V3EiqUoNVgSRZ51JCEbGd-SO-lASwNc-x9n8WqxSjkMIFR1uNQmNqW_o)

Connection refused: me sale error debido a que mi sistema llega al nodo de destino, pero la conexión es rechazada.

  
  

Contar el número de ocurriencias de condiciones de carrera registradas:

![](https://lh7-us.googleusercontent.com/BaGIHphqaD3DDcm4H20EazJd3u9ciZkAJ3acAdsNnZH0eW-o1m54CEjdUgd0Hu8n4BhumoUPlTfg5kMcBtx5r0AV1zX7a-hEl0Y43WY4AL_fHmIFCJYBwZB-u1UMydEq_W0enXKwZvF_-xnHuMvAuMY)

Extraer IPs que han accedido concurrentemente a un recurso:

![](https://lh7-us.googleusercontent.com/3FAuaE_aer2LaCTUSbbkEb0Jm0T_XxJyCXkVSQawvpmJBCFq3zAgiuPgVuVS24Dv_dlT1M3s1454tIX7mxPq0LnPlENJI_-HJMcxIg2swSt08xeXHGup-JrOA4zHOXdciKpNL2rpMVjLl5nLnM4paPo)

Automatizar la alerta de sobrecarga en un servicio distribuido:

Monitorear errores de conexión en aplicaciones concurrentes:

Validar la correcta sincronización en operaciones distribuidas:

Monitorizar la creación de procesos no autorizados

Detectar y alertar sobre ataques de fuerza bruta SSH

Identificar uso no autorizado de recursos en clústeres de computación

  
  

Pipes

1.-Monitorizar el proceso Apache2 mostrando solo algunos campos

![](https://lh7-us.googleusercontent.com/oR9CGmKw81EhiFa_K8Au703diEJ6eoa4Ip_2YTkrv5d1AnT9ccA6q6_zb85uD4GYBsoCachGXnnSHDPzYBaWoqA1Wew-wk9fUuNOdKfrPlT9yTRBoW800Pf4sYx6Q3rf51GYG_frcT7CHebsIBzw3cA)

![](https://lh7-us.googleusercontent.com/KkB3QdVg8m1JBcVmHw6dQYPW1Bt77y3gukdwUyxS01izCpVVJufPLew8pWSkwv2VFEBQ889tlgDx0w8Agn-Iq9DE4ocxpC4qxE5oWNWJI4-GimnbovbMvM86sgEI9Oe_2pdB1IRAw4z-Ef7W5OGrYNU)

  

2.-Encontrar y contar los errores únicos más frecuentes al final de las líneas de logs:

![](https://lh7-us.googleusercontent.com/V_v4HxTOvXuAetHuf7WWuWQCNM9JvWq8F8aUCRGC6L8iqCZHT9rk8oCkmyIIOV3cD-tPWwIf6qrEix-y9hVLFRNm_11Wy5UaA53OE9c_wPHIdl6IIKnUWAvstiX8JAN0tU_0Xt6JQPNo5MgPDVucbf0)

3.-Reinicia servicios fallidos automáticamente

![](https://lh7-us.googleusercontent.com/enn5ZynTqF_kdRql8nZNr3dfjUgi780r9VVYtm1PlDcH04Ojmc0L-hQPJvfXHLEsUoo02m1jKT3Hm9JddxyH8mKloCeOan1WaqOlctNx2gMeovtHbtd8_ztFQdMtFl_lzW0JZYB3w0YG4MrJ2l3YC0M)

![](https://lh7-us.googleusercontent.com/01szrceO3ipH0X77y3BcYOPQjB9F4MN0BZNs4jNyPzmzCApQzHxXcGQsnoimZwLtBsksnmZibUI6FqDnMePtdPGiV3T11BAl7lOuikXFIDWwNbI3uPSoneUVBMkFCWyT1boo9DPVgMnoq9amZRKR64w)

4.-Enviar un correo si hay procesos con alto uso de CPU

![](https://lh7-us.googleusercontent.com/6LyYVPqVBIT89JYEyX88jyD5dBxzGzK4GTkkAEHexgjVg3VKWhgW4_j0T18L_Vz-b_LYXO84gvzLLRkayK-Oplu3pECFVr0an1DtncqcJXgQrtaL6JOWYCfpks0LJbACguAVCntP7tDPsu13csJfilc)

![](https://lh7-us.googleusercontent.com/tWCmcZM1cpTjAXdvlRpD5xEdMpBdMZIz7j22gAwY1ftErHIFyDq1MD6sk4F4eXlIG9T355b0t9kA68m6Cfs8atXOLi7PKvOeXMRhZgqER42UY_j1UAP946f4OmiciyXG6tSm7aSISmdsGm5f30Hkcbc)

  

5.-Buscar errores en logs en un nodo remoto y guardar los resultados

![](https://lh7-us.googleusercontent.com/kEomrSbq1HpjYhUuamcT0y-Jo2lICFIODqhjbDBoBg2-OMvD_bRWq72JJZHEGEdiEBxTrrx0mbipKLX9cf4oKAJfFkOV6-ROuU_wnWWF9m6Q4WZvUWJVKZuJy1jW_Mf5lfhUrUJWHX3ckvutWUUtfbs)

![](https://lh7-us.googleusercontent.com/NQHzqcrm_GW1AgHbP1p8lhqHE82gRrynEYJBoAQUwNsoDGk4hpPly2mbgjY3numRuhfl4zPNZ7pa3WwxVWsKeWoPqu2jPnA5Q7e8bSOLutAOzvoifWfF6pEIuUblWJKwaqjBA7a_RdbgFpMbteVLDr8)

6.-Verificar la conectividad con [www.example.com](http://www.example.com) y registrar fallos

![](https://lh7-us.googleusercontent.com/Kbmdcw5lJg05xIvWOV82W1s7Mxrn0zavP9H6hAnmQi0E5Yk57Dktqnyuci5smj1LXeb6aXDBMhVv8VCEq7VS8eBP60qZLK5hobLLrPSvTP0SvqhhgII6iNHi7MTgk3hOcHySZ8bLI1t0pbQi8DSmlZQ)

![](https://lh7-us.googleusercontent.com/HVU1ssWpkx2CecgOH3xIoOTFnxt_yQDHo_tPmCrfKm1tQFCKHouQ7ni0-gIUkvMw2J_GT8v8JdSPiAraF3fdYg5A6_pxoNjl7V3ebcd5-5ip78HqWhsvqY5BG3TBPHzWUkITOrFzkGRqWLu2j2euvcY)

![](https://lh7-us.googleusercontent.com/TNfToLBG8uJ1I-E6H6hVpf2E90CecKFc_944UDrHFrZItlD6QQowXo9b2utXuWtN-760DO5sHNXyYLd05NhoZ8vVfZQJZttOwBnCjDih85u4F3DBJGCMarMxxLFnnXAY7nBBN0PlYTQ00rVFom4slmQ)

7.-Calcular el uso promedio de CPU y memoria por procesos httpd:

![](https://lh7-us.googleusercontent.com/b2ZHimHr8n7-Q9kM-35iZw3dqpOJYQT9yPSrCbhuFSlVg7IJ8L1pUoGfWREzgJOge-JnV-pVxEgaZybHxPw8391raTIKLl1MAxhJQXCwod4BvnXue7eA4EOy9Jc8BwMop16h5GElf0lLEVZm9II4CV4)

![](https://lh7-us.googleusercontent.com/jIxfAb_4lOAkVCOEx2UZvJlrTbTwjx4dvUkVx2hr2h9_Gl6TrakX7VW85JepNdnGksiPjiFJQoiGP-B0kccYmwafK2t13kUDBYWaqZXWUGMYsuiUGqXzeBkXY_76zkAF7NCMNVh_uPnVKYpMT94px6s)

8.-Crear un archivo tar.gz de directorios que superen el 80% de uso:

  

![](https://lh7-us.googleusercontent.com/2KdF_pcAg7lpJLl2QCLtO5fPhUHOYb04eZTm47zUtenuKOPGf8CYn3TwmmhVVqxvRS15Q0lZn7iO0zv9tdgWAuUX4oTBVIr5AJDdSme9ijx2KUsLTRAzD2vnZwC468FMuwD3jkeG5tvwQPoriAUbqjw)

  

Script 9: Monitorear el uso de CPU de procesos específicos y alertar si superan el 80%

  

![](https://lh7-us.googleusercontent.com/s3zq4OsdXgnZzIhbK5WqIiJeu76G2T_GhZdVGA4m6nIclDd-B0AgNEmMOCyVjNzL2pwv-eOmuZZGGIT127DpUoA5wgU0i4Mk_MG1A8DIff8OITtp5Kl7PDRC4ub4ZUmOv22qbv9VmBIpzpNJ9zFV6PY)

![](https://lh7-us.googleusercontent.com/3N4ZUicL9mkb0nsvUF91R5S9ELJyVA6Sv0D1OcKJPp__nm7pHVkOKXpVPdqW7cpe8-CEy6Q35J41PquIgR_bxr06XG7vuoouIzQfwg-q7Oi_-d6YwV7pnFLcRzx-AGovzcXxs_3Vy7zTzrM9B4NFD4s)

  

Script 10: Filtrar y contar ocurrencias de errores en un archivo log

![](https://lh7-us.googleusercontent.com/O4PqYLXOse7YNjnTP7oAMRRbNi6eixUDCRxsfJ5-qA6iSMJycLh3GmcJNKxLgOgtz9j9Gseb8r2FlJ9Avvwgdz4g_ZrsFejsJzfxjYs2_Lf03UJ9oBOnniCGUw8ah6jOupCGVg2rZeygQuTyIPRc34o)

![](https://lh7-us.googleusercontent.com/itO2WIKxEv_qZTFmmOZXK8rGJn4aLnAWqYo-kG5oH0yIY8S-13fhnu-t8TGZ5IpGWa3lp5QvxmXbVvBheZGGjzYQuy46nR4kCEA091UZcgtSjDO58savCFzez3gRs8A56L3HdA1oAb2C4hXznOnosEQ)

  

Script 11: Uso de multiprocessing para analizar logs en paralelo

![](https://lh7-us.googleusercontent.com/bImyE0WFpgAYp67KWW2BQImc7hz0YIYuNVarg6JKD04Xm8pbMs1ZOqMib_w1Vpl1RexyCInSYEX2UQTIVXSpmkYjuVlt7a9GpabgwoDyQ0g8jASMs9irjPmXhhno-SqYKYGGPWTkSSv0oJUl2mRnH9k)

![](https://lh7-us.googleusercontent.com/0A2poDx2Uwai94tXi31D1D6SIDYgkDpL8-kJbtE-8mAThJQfXd3gAsCLtQh27Fm6FbZjVkqOkLp1a8Jb8LSIwOTPljsS2OH0rgl122PuxA0xXUgy3aiXfPzl5ebhKjrHEWelnhwgGm2RSMd9WXcl1pQ)

Script 12: Monitorear cambios en puertos abiertos con netstat

![](https://lh7-us.googleusercontent.com/ARBVOsK31NDiIrOCOsnjTLGtCnh-qyBejG82minZmPJjEE7e0savpiKehJKq1_KjB6OwBm1nYo-Tb7BthXq3gOkHE41IBLqmOCNTQHCckrgbZXocbKnD_mdS2ls0Gkew23natxo5IJ0C0dUxWHPDzJQ)

![](https://lh7-us.googleusercontent.com/hNktoUVI_2EXIyXPWAopdlPE8vlzZlA0SOEPTVOaUrXv6gjaJ8cGIubgXFK6h28aMD6Pn1jE-uMQwmBG32hIqY2-xp_UM1v_Ku0HD4tPUyXnEtb1OCZlvTW-c1sp3pC-Ri2JORfoluEZJIQpl3A0w04)

Script 13: Calcular y mostrar el uso de memoria por usuario

![](https://lh7-us.googleusercontent.com/azKB_VZ0r4IDqxGTCgE_Wd7UpubBuLut-AtXLec_rt9ePadtzGNe2e0TQ7oQyHZVvhs22ByoFAtlHGczgh9zBfWnSoRUSJOVLLW1vp1HPuSMdN537El7Skk8zYAYkTe97ud8Eazrx2cLXOl2mfmWOIY)

![](https://lh7-us.googleusercontent.com/7-GrGiEDBH3t66hREyQ3NFPyksfdJbp7Hbg00RteMM0mn_vlSbtJqye5IXLCOBp-W6iTkZ-VCQGsJ4cQie9odKgPzikx6cMNLXRCdMiCTHgvLLk0y6AwavwZaS-W1CdtbtJjH3Vo-H1FOGJzfphojkM)

Script 14: Registrar el uso de CPU y memoria en un archivo log cada minuto

![](https://lh7-us.googleusercontent.com/Xyzb1b5xiXLdT_Rh8TNYiR8txZuWWMEuMkb7iLDQBAtIJQf9ZoVfAB3J-RDlx2syMqHyau7kZTMw0j8n_uH8oxp6xbWT08uQnHC0aYQMli_tdl3e1FK0bHnaaHBw7uPPMjUiF035MikgXyg6bZFTGKE)

![](https://lh7-us.googleusercontent.com/gN_dtH_HEViFC5U5jW28pPUwgCEPdk89CJMawgpTb_2mbmHJuXEbk2y-h8Z08e2dOgxoAhNwcBijMv2SKA3PxFK32q0RjU9ULfFLqDS9VqR41tAOkfQccaCyJqWdUH2Ul7C8138-7tGmaBYs9bOBo1w)

  

Script 15: Alertas de CPU en Bash (son idénticos)

![](https://lh7-us.googleusercontent.com/8ps6RPSHskdNZCIlrvbb3M6PQbWZXzvQ4XTJ2WdHrqBZf8-e9wxixhUq__ruhTW44vXCYoCG77tVZP83Xr_7gFv5M4I57irDvFb9HoHWY3XpOZ_AI9oZsav0O-dRyHB_ozbwfDvIJ4oBIO5NYlbTQS4)

![](https://lh7-us.googleusercontent.com/8Y2R0peLv9BvomxyBvwCF-n9fpjqwYISEAb22juZZPlYlQqHvCQUFoGWYZ5AvHq4TQyHcP_V00eksN5tRVvxQzoQGyoDnMZcZETfGdkbPkRk1fRQ-1r2NB1EJsmoVHe4AeVXiZPPIh3FYVLW-OU55zM)

  

Script 16: Uso de memoria por usuario en Bash

![](https://lh7-us.googleusercontent.com/eHd18FhCJPhQFd4O25JGQ2CwcH0afEHVkjnAfI6-rh9-cwtt340xZPwa7Ibi2wGDfmC7EWpKjPHDUSIvRGLGOsLUlecpI-L13EHOAizhLVSGyeU-a-IfiJKBbXPokXnTmM09r_KkUaga-nnGyjIdeqQ)

![](https://lh7-us.googleusercontent.com/C6t4OC_UR2inAg9hc217XopYbwLeA4Ncl8KZvUt-iuhpfuiD0QWzmvUXvYYPyM00CPY8LRtmroHv4cHp_oePv_d3_DOPlxxNq0RXCQJil7e1XodHqpbhu2n5fwknbtEYHwrrk1BFIX-_W3psWJXDJ28)

cript está diseñado para alertar solo cuando un proceso supera el 80% de uso de CPU. Si ningún proceso alcanza o supera este umbral, el script no generará ninguna salida.

Script 17: Top CPU y Memoria por Usuario

![](https://lh7-us.googleusercontent.com/6RvcuBD57MkHt-JPrV2Nb92blpsAGhrOy1HgdxxLlHvqdHOWRz9JmqCXYpRsl3nQUnxusP1PpowD8MjFWf6_XQaDinZx3r-VZxmjjzlGnrTAjx2kF8rB8htHbtpmLxy4Daqnehf3aOt_ls-3tdWt8xU)

![](https://lh7-us.googleusercontent.com/GoSVXysTghhEfquZdzPQcnPCYectWPgY4GKk8fK1lSc8S6G67X_nigRFUOaqf2itcJPjPz0H_IIY7Z5Huz21lktSjjPeq5GD1VcT3NvGDD7Jfrqgo-SohsVm2OHjn2cJIDtcohqwYS3q4nk_6mT0ag8)

Script 18: Reporte de Memoria para procesos Java

![](https://lh7-us.googleusercontent.com/mYHLTXlJzCoQiW8Pavj4yvGh2Mv7H_Dre2o4EXN5x4fcha_W8eogVECY8zLXwZp-LzDa4Wrc30a0UFRfeXkMYLgVHsw_exl8WdrcHN2znnim7DzNSG2dGqpeAo5RqAfnc3yO4Z2bJ2GbRuzMGLwZWH0)

![](https://lh7-us.googleusercontent.com/_ZvdqOlOXAlEVeRkeGW2ES7fDviPJTZZpgFHNvud7iZsw_HTyZ-zACos2RpcrQg2iubzj2GkBJXFLHNctefwKjduF-ZfRKvxN51wv1i77q14Nfe8v4CcV_M2JbYW80Mmi_o0G1v9Tfwz23HkYuuqWKQ)

  

Script 19: Top IPs accediendo a un servidor HTTP

![](https://lh7-us.googleusercontent.com/gtdAWk2BXq_C5-E_YSH_c9ok_GhbnNq15UV50Uxf3wgCWAa5EVxIRwg2MBsNQtXyJkgDWIMnnLrQbIjCy--zBTX3WjzuFCXPZM09KN7TW8J44ZEdGCB88eS9i-YTlqhhEG9SXwJ6BHZB340xg3qbgnw)

![](https://lh7-us.googleusercontent.com/Idjtn5uu1GJgx_J2v3XzNTBEq0FmlocEbBsokbIRwfGA1Aw1mp5gYz7kWMRiFynj7fWYuKO22hahuKwnaYkh7DgSmpKBoegoOWzshS-T8z93FOfYrDrafP2EgXDrzYLQsYp5HmMwomq4-w9ZySCxRjk)

Script 20: Estadísticas de red para una interfaz específica

![](https://lh7-us.googleusercontent.com/zESb4J3yOJrtVdU0HVnI94B0QdVvv6L8SQuH3i4p7OWKFHvVuXZaR0UGtiujrfABS35y6L0uDqF6D48rW6vPQOK6EPyjovmWHrT-hIWCG9DtJS8IYLi8aqwJ26D4Os9Pxw8jtbQNJqBvqDXO-m5lgZc)

![](https://lh7-us.googleusercontent.com/sijDjTIWMilDBpA3_Ae5EApZE0760FXYhfsuW_TZatJRJRZKtUQM5v4A4byUBtG15aoPdlEk96TkUseKGY_ol77LhKz1HHX4vOG629_GlAO41ioExH-8mvH_tRV62PSRJfiktC3LB62ZySXmn2KNSnU)

Bash

![](https://lh7-us.googleusercontent.com/SUEFf6YGTW-6PsumRkk6IqudQZZCzF3zE0nscG6c-8e6a7Hl0ELCJBljWWZQXL8LKX6hqXSWIvxeaojiMb41RCLLxaSZ5v6i0P55ZUT9wgtKpo9ZPdrHxcnMNMUaZ-qLFnPuZuFNPvq7f9U0NwuepfI)

### 1. Monitoreo de Procesos

![](https://lh7-us.googleusercontent.com/AkPr9ItWuEqG3Rb_wor2OYO-W1U01g_ewOESpnyvesb0xBpM1FePpvhTcpzPROGNWtozmHzIIJ6jIEOh0iG7LpDg-7OPE-9B9S2ErkH-bXev4fyBivhh06L9gGarggyqrLt4NV3P69sxVug0n_YFtxc)

![](https://lh7-us.googleusercontent.com/IbPdXpkpMoA6O1weKs7cJqpKJ1uR7xQ5U-Md0rU0i--NDlvVguZDFf5bGihlppq607CD3BA1G_gbqg7O7i9nq-QUTkIZ22TceELsxW32zkWPI9NrBpIO2hsYD5fppxTxqZ2Piwdw6vPK7ABcBsNPKm4)

### 2. Backup de Directorios

![](https://lh7-us.googleusercontent.com/V3-GSupXI6MPR4RIzHlAwRiFY7NrR937zzjeBFiHOYe86b3V_9nhN4iivkpPeaMSwXjd3fn08P9TKlVIeInNCM_g456nuBfZUnhF1i7HTmIpaNP3A9h-vbbRKMaiJ_2aW886FgPKduDLCc2xFg8EXBI)

![](https://lh7-us.googleusercontent.com/VLFzt7RUXRgkN4CbZ_cj3oOogimSrybaKLisk1-kPmua5bs-7ZDStWncvVrctMZ4dUzmfWCymlePQf4mCVlIl_9xTkTLmqFz30NKFDoCn_B88h2T2B5DRZXFnHgXlBVWa1Q_7PAL6tf22Vsjdvxcgrk)

### 3. Distribución de Tareas

![](https://lh7-us.googleusercontent.com/LnwSmrt_paGB__dwPHH8mBxeoAYKER0uopkhFofPbnEDBdAyGJj499_XxSTKtNrVxU8kLSZW5AiuN7P6gvCP9aV-6o8HfGE5zSp9BPrU-U--AlHJFAF562QnAqAkq4vD2hzIKenFUzUF9-CzDCdTAKE)

![](https://lh7-us.googleusercontent.com/xdc7_HWOkwnK_Xhc37i5-X9wXzfKM5frO2afCeiMvhd-yoPdhx9hBmwx3h_av9ySId4aFDk8KStdpEcH29NbNhhexsz25R0lc5qWA4omne7RJiVf0GGyLhGUII56vRSI_ybr4l1hDcxtRzYq0dd2jjk)

### 4. Control de Acceso a Recursos Compartidos

![](https://lh7-us.googleusercontent.com/ImP93JZFNWdUkw9f5obWnx6U-oD4RA0oAdHOnCAjy5HQ4BgS6Xsz1O6_V7HWc34m0CGs65lj5q0lNoC2LNUI1fbqUS9pySktMYg3nFKDjhSbm-SQoVoCxpchNd_yYk7a8YFZxkwMH5vqoPzsK8nQz-0)

![](https://lh7-us.googleusercontent.com/ioTub2a_kI3qwAvwz4rScWFSepYeEgca4tJHOLFMmANT3Is3jDCGXNxp3tVb2lYMCQspeHNEI5IKnvU18o0FsXP3bT6ReBD7BiSX9tCYlfYBpLMyXv5iEfuDgB6RZDBdLoSjcaZk73ZxVKrjQvEBA7M)

### 5. Recolección de Métricas

![](https://lh7-us.googleusercontent.com/dImNbAbN1_as4XC0MqZlaPOZazuyahZnTiGHdkTULLn9eJUF02AxgDCfdhYSJZ9Fb35lOuk-QcC07fq2IcG0xDNXELdPE_mWneCNBaJ8mLiswJLaofJ3QepG0x5R5Z1wlAuAx0-lovRETdmJNyj3IqQ)

![](https://lh7-us.googleusercontent.com/7bsZRpp79QH-nrNmWXy2U38RXMFKyupUKtsbyoOlRsk8t8901oI0Yz4LmWbzwdTeS6gE1Nrdg28e6hvi_ctzoaP4_unE-jEw7h-zeG4b-PfP4_XZFWvgRXjb_VjAokXp4BS6tuSQZAmc3GPJSMgwe6A)

awk

Ejercicios:

Pregunta: ¿Qué hace y cual es el resultado del código anterior?

este comando usa ps para obtener los procesos actuales y awk para imprimir solo ciertos campos (usuario, PID, %CPU, %MEM, y el comando):

![](https://lh7-us.googleusercontent.com/R2mhM1-_i1SEYlrhcpSJ1Vfb-quXBR3mbEqQauJTrMsrjUiXZKT5aZWytyp7orLPJEcLXMrLK5V1JNrOkkxOsR0rE-Al5xx0mFnmNGsgiaW_GcFNz-lIB31YyW-MhWvkOKt-jeMMe-l_OcNhjgtL_ms)

  

### 1. Filtrar procesos por uso de CPU o memoria

![](https://lh7-us.googleusercontent.com/gL4XPkl0seBM--shyB9xAQKdUpmqElE93cqYEvbWP4M90U_hHuX2NSUYXLBBTxa1ZDvOgzk90WFhegIZMnqVpqGuf_XvJ1tShUryowdmcKS7x33WSzZwbrI2_kbLRuZE82gt779LuTgaU5leX6mp02c)

### 2. Dividir syslog por tipo de prioridad

![](https://lh7-us.googleusercontent.com/4bpKYYCizCfz7oGG_TkwdOA54cMB7-hRJuKCL9pMmd-_1MGjmA5WDqUK_nERQHrKaqw4zsgegwCPjw97XOTb5t18pWnYNZfUnM8FivcJB6l-ohTGYrIcpErwfyUTOv4SWQH_lZ42UHBpBvKiZaNFRkM)

![](https://lh7-us.googleusercontent.com/wTXzlefV5VoS323s67Y9KE1oxqWg54Utf_cBigliG564I1cS_YCQqVtX6B9NZ_5SfHiTIx4xzmXxMG_qlUS4KHDhEc1FBsNwgqOYUWzQ93zs9_4HxN6wLGJlXznEoJS-tve_dYFWfK96H52GveEJyys)

### 3. Contar intentos fallidos de contraseña

No hay intentos fallidos recientes: el sistema no ha tenido intentos fallidos de acceso

![](https://lh7-us.googleusercontent.com/P-sapv-XclCYQ2j346JecmLQBKkFb6P-e1NvZuPxmfZELxe3k6vl1v3yPNIu4UTDpaXJylxL2qBpx7k5lnzxPofZAnINe2n9pcKxqdEL1ppQlB3Susd4wfJE28lc3V9vx4hcRfZyAAAQZLa97_DsdjE)

### 4. Monitorear creación de archivos

  

![](https://lh7-us.googleusercontent.com/QjyhgHACKbhvQ99CsmnLacGUEwrudwCOZVqDbPAcdOnzbFUafPIBQvjcpqsMocSrfj16z81Wa-0xawahXQK07hqRXi6lFTS-U3dEXCspP78tzS0GGylR0x4pnfPLtQhPASnEgJUhmOPq2an2htVMfTw)

### 5. Calcular espacio usado por archivos Python

![](https://lh7-us.googleusercontent.com/HtLwfopXcaa77vzDeTvaUkVM5NrzXjXu8u_cwYUyi7aF_lTQtkVoNVzo4DIy8eBtU2NNBRlE2s48jotxZxSzHc2q6usWYK50l9VUU_D-wmDmuZG7C8K0iKZlB1xmdvVHj5acvD_xATsUtICFLLucppo)

### 6. Calcular tiempo promedio de respuesta desde un log de acceso

![](https://lh7-us.googleusercontent.com/ZjAsrSE1Q7zxLRR2LmIrNz8rW0xseUK3mo52d1-zjt8Mh3Gq6G61p9usOZG8x9CrCRHoiohuDyVJlUjBremua79PHxyBHRFBAhiJgpnmH9Ppf0aOZ7Jek81dcgXENmDcv695y6wfj4iFXNJX1XoU8vM)

### 7 y 8. Contar procesos en espera y ejecución

![](https://lh7-us.googleusercontent.com/AExmjPJCB98v5RV1yl3y48hTSRqePy2P0mO7mf3WpOq9MoiUpzEKEAdtP3h4q7h2y7VZ1iej7UzRiRAczHiKHFTs8myimVd6nd6lsRNo_8maeLMKw2kJgDZEcyjkG2hz3L5vIL3Mf0QMZDLYhD_h8yQ)

### 9. Alerta de uso excesivo de swap

![](https://lh7-us.googleusercontent.com/wqxkf4cecP6RjoZciG1Ad_2OmvyjAf6V50Sm-ALM0XRjcaVLOn49jwGUrDhiVtSKWm5J0meqoX5qmcUbBV1w3tRUp2MCuJ7ho5GH1JwYy8JXksr30ctiQSFQwtNSs0x8tClWBnvaRvaEJUfLKEPlN40)

### 10. Uso total de disco por archivos no directorio

  

![](https://lh7-us.googleusercontent.com/w4y0WPaeA9RZnUXVs6devWh2ijEI5-wzkVRAEwNpAppOxaQTgAma8RCBXcf-u6ZiM5RakriuMAiV2pueE33BVepGXCcaWCsFhjuAYfTs6HOv9CwY0fPv5frv_EEcYJ3b1K067Jj2TBEbV_x9mY12iqs)
