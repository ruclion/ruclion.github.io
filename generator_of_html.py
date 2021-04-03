html_out_path = 'index.html'
html_f = open(html_out_path, 'w', encoding='utf8')


def print_html_each_speaker(s_id, speaker):
    no = speaker_N * s_id + speaker
    print('<tr>', file=html_f)
    print('  <td>'+str(speaker)+'</td>', file=html_f)


    if speaker == 0:
        spe_no = 2 * s_id + 1
        print('  <td align="center">', file=html_f)
        print('    <audio controls>', file=html_f)
        print('      <source src="SPE-wavs/wav-batch_'+str(spe_no)+'_sentence_0-linear.wav" type="audio/wav">', file=html_f)
        print('    </audio>', file=html_f)
        print('  </td>', file=html_f)
    elif speaker == 4:
        spe_no = 2 * s_id + 0
        print('  <td align="center">', file=html_f)
        print('    <audio controls>', file=html_f)
        print('      <source src="SPE-wavs/wav-batch_'+str(spe_no)+'_sentence_0-linear.wav" type="audio/wav">', file=html_f)
        print('    </audio>', file=html_f)
        print('  </td>', file=html_f)
    else:
        print('  <td align="center">', file=html_f)
        # print('    <audio controls>', file=html_f)
        # print('      <source src="SPE-wavs/wav-batch_'+str(spe_no)+'_sentence_0-linear.wav" type="audio/wav">', file=html_f)
        # print('    </audio>', file=html_f)
        print('  </td>', file=html_f)


    print('  <td align="center">', file=html_f)
    print('    <audio controls>', file=html_f)
    print('      <source src="Zero-wavs/wav-batch_'+str(no)+'_sentence_0-linear.wav" type="audio/wav">', file=html_f)
    print('    </audio>', file=html_f)
    print('  </td>', file=html_f)
    print('  <td align="center">', file=html_f)
    print('    <audio controls>', file=html_f)
    print('      <source src="Std-wavs/wav-batch_'+str(no)+'_sentence_0-linear.wav" type="audio/wav">', file=html_f)
    print('    </audio>', file=html_f)
    print('  </td>', file=html_f)
    print('  <td align="center">', file=html_f)
    print('    <audio controls>', file=html_f)
    print('      <source src="Big-wavs/wav-batch_'+str(no)+'_sentence_0-linear.wav" type="audio/wav">', file=html_f)
    print('    </audio>', file=html_f)
    print('  </td>', file=html_f)
    print('</tr>', file=html_f)


def print_html_each_sentence(s_id, s):
    print('<div>', file=html_f)
    print('<table>', file=html_f)
    print('<tr><td> <strong>Sentence</strong>:', s, '</td></tr>', file=html_f)
    print('</table>', file=html_f)
    print('</div>', file=html_f)

    print('<table width="95%" border="1" align=\'center\'>', file=html_f)
    print('<tr>', file=html_f)
    print('  <td align="center">Speaker Id</td>', file=html_f)
    print('  <td align="center">SPE</td>', file=html_f)
    print('  <td align="center">Zero-0.000</td>', file=html_f)
    print('  <td align="center">Std-0.002</td>', file=html_f)
    print('  <td align="center">Big-1.000</td>', file=html_f)
    print('</tr>', file=html_f)


    for i in range(speaker_N):
        print_html_each_speaker(s_id, i)


    print('</table>', file=html_f)



speaker_N = 11

original_text_path_list = ['hanzi_no_id.txt', 'english_no_id.txt', 'hanzi_with_english_code_switch.txt']

text_list = []
for p in original_text_path_list:
    a = open(p, 'r', encoding='utf8').readlines()
    a = [i.strip('\t\r\n') for i in a]
    text_list.extend(a)

print(text_list)

for i, t in enumerate(text_list):
    print_html_each_sentence(i, t)
