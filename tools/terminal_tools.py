import subprocess


def executar_terminal(comando):

    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            capture_output=True,
            text=True
        )

        return resultado.stdout + resultado.stderr

    except Exception as e:
        return str(e)
