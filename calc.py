while True:

        hora = float(input('Valor da hora: R$'))
        tempo = float(input('Quantidade de horas trabalhadas: '))
        sb = (hora*tempo)
        sm = 1412
        inssp2 = 2571.29 - 1302.01
        inssp3 = 3856.94 - 2571.30
        inssp4 = 7507.49 - 3856.95
        vt = (sb * 0.06)

        if hora == 0:

                break

        print (f'Salário bruto: R${sb}')


        #inss
        if sb <= 1302:
                inss = (sb * 0.075)
                sb_inss = sb - inss
                print (f'-INSS: R${inss:.2f}')

        elif sb <=  2571.29:
                inss = (sm * 0.075) + (sb - 1302.01) * 0.09
                sb_inss = sb - inss
                print (f'-INSS: R${inss:.2f}')

        elif sb <= 3856.94:
                inss = (sm * 0.075) + (inssp2 * 0.09) + ((sb - (inssp2 + sm)) * 0.12)
                sb_inss = sb - inss
                print (f'-INSS: R${inss:.2f}')

        elif sb <= 7507.49:
                inss = (sm * 0.075) + (inssp2 * 0.09) + (inssp3 * 0.12) + ((sb - (sm + inssp2 + inssp3 + 0.03)) * 0.14)
                sb_inss = sb - inss
                print (f'-INSS: R${inss:.2f}')
        else:
                inss = 828.39
                sb_inss = sb - inss
                print (f'-INSS: R${inss:.2f}')

        #irrf
        if sb <= 1903.98:
                irrf = (sb * 0)
                sb_irrf = sb - irrf
                print (f'-IRRF: R${irrf:.2f}')
                print (f'Você está isento!')

        elif sb <=  2826.65:
                deducao = 142.8
                irrf = ((sb - inss) * 0.075) - deducao
                sb_irrf = sb - irrf
                print (f'-Dedução do IRRF: R${deducao:.2f}\n-IRRF: R${irrf:.2f}')


        elif sb <=  3751.05:
                deducao = 354.80
                irrf = ((sb - inss) * 0.15) - deducao
                sb_irrf = sb - irrf
                print (f'-Dedução do IRRF: R${deducao:.2f}\n-IRRF: R${irrf:.2f}')


        elif sb <=  4664.68:
                deducao = 636.13
                irrf = ((sb - inss) * 0.225) - deducao
                sb_irrf = sb - irrf
                print (f'-Dedução do IRRF: R${deducao:.2f}\n-IRRF: R${irrf:.2f}')
        else:
                deducao = 869.36
                irrf = ((sb - inss) * 0.275) - deducao
                sb_irrf = sb - irrf
                print (f'-Dedução do IRRF: R${deducao:.2f}\n-IRRF: R${irrf:.2f}')


        # vale transporte - pagamos 2 passagens de no máximo R$4.45 ou R$8.90 por dia.
        # são 26 dias trabalhados de seg a sáb. 8.9 * 26 = 231.40
        if vt < 231.4:
                vt = (sb * 0.06)
                sb= sb - vt
                print (f'Vale transporte: R${vt}')
        else:
                vt = 231.4
                print(f'-Vale transporte: R${vt}')

        #FGTS
        fgts = sb * 0.08
        print(f'-FGTS: R${fgts}')


        salario_liquido = sb - inss - irrf - vt
        print (f'Total de descontos: R${inss + irrf + vt:.2f}')
        print (f'Seu salário líquido é: R${salario_liquido:.2f}')
