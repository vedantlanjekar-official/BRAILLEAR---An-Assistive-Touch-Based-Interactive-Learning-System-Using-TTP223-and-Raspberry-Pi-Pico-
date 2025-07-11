
import socket
import ujson
import pygame

pygame.mixer.init()


audio_files = {
    'single': {
        'A': 'A.wav',
        'B': 'B.wav',
        'C': 'C.wav',
        'D': 'D.wav',
        'E': 'E.wav',   
        'F': 'F.wav',
        'G': 'G.wav',
        'H': 'H.wav',
        'I': 'I.wav',
        'J': 'J.wav',
        'K': 'K.wav',
        'L': 'L.wav',
        'M': 'M.wav',
        'N': 'N.wav',
        'O': 'O.wav',
        'P': 'P.wav',
        'Q': 'Q.wav',
        'R': 'R.wav',
        'S': 'S.wav',
        'T': 'T.wav',
        'U': 'U.wav',
        'V': 'V.wav',
        'W': 'W.wav',
        'X': 'X.wav',
        'Y': 'Y.wav',
        'Z': 'Z.wav',
        '0': '0.wav',
        '1': '1.wav',
        '2': '2.wav',
        '3': '3.wav',
        '4': '4.wav',
        '5': '5.wav',
        '6': '6.wav',
        '7': '7.wav',
        '8': '8.wav',
        '9': '9.wav',
  
    },
    'double': {
        'A': 'Example A.wav',
        'B': 'Example B.wav',
        'C': 'Example C.wav',
        'D': 'Example D.wav',
        'E': 'Example E.wav',
        'F': 'Example F.wav',
        'G': 'Example G.wav',
        'H': 'Example H.wav',
        'I': 'Example I.wav',
        'J': 'Example J.wav',
        'K': 'Example K.wav',
        'L': 'Example L.wav',
        'M': 'Example M.wav',
        'N': 'Example N.wav',
        'O': 'Example O.wav',
        'P': 'Example P.wav',
        'Q': 'Example Q.wav',
        'R': 'Example R.wav',
        'S': 'Example S.wav',
        'T': 'Example T.wav',
        'U': 'Example U.wav',
        'V': 'Example V.wav',
        'W': 'Example W.wav',
        'X': 'Example X.wav',
        'Y': 'Example Y.wav',
        'Z': 'Example Z.wav',
    }
}

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print('Server listening on port 12345')

    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024)
        if data:
            command = ujson.loads(data)
            character = command['character']
            tap_type = command['tap_type']
            file_path = audio_files[tap_type].get(character)
            if file_path:
                play_audio(file_path)
        client_socket.close()

if __name__ == "__main__":
    main()
