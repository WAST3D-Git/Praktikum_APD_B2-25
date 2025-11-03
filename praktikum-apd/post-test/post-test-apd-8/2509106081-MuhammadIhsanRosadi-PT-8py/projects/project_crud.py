from prettytable import PrettyTable
from textwrap import wrap
import inquirer
from database.db_config import projects_table
from utils.helpers import clear_screen, pause

def lihat_proyek():
    clear_screen()
    print("=== DAFTAR PROYEK ===")
    projects = projects_table.all()

    if len(projects) == 0:
        print("Belum ada proyek.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Judul", "Deskripsi", "Software", "Deadline", "Klien", "Status"]
        table.align = "l"
        max_widths = {"Judul": 20, "Deskripsi": 30, "Software": 15, "Deadline": 15, "Klien": 15, "Status": 12}

        for i, p in enumerate(projects, start=1):
            row = [
                str(i),
                "\n".join(wrap(p.get("judul", ""), max_widths["Judul"])),
                "\n".join(wrap(p.get("deskripsi", ""), max_widths["Deskripsi"])),
                "\n".join(wrap(p.get("software", ""), max_widths["Software"])),
                "\n".join(wrap(p.get("deadline", ""), max_widths["Deadline"])),
                "\n".join(wrap(p.get("klien", ""), max_widths["Klien"])),
                "\n".join(wrap(p.get("status", ""), max_widths["Status"]))
            ]
            table.add_row(row)

        print(table)
    pause()


def tambah_proyek():
    clear_screen()
    print("=== TAMBAH PROYEK ===")
    try:
        judul = input("Judul: ")
        deskripsi = input("Deskripsi: ")
        software = input("Software: ")
        deadline = input("Deadline: ")
        klien = input("Klien: ")
        status = input("Status: ")

        if judul == "" or klien == "":
            raise ValueError("Judul dan Klien wajib diisi!")

        projects_table.insert({
            "judul": judul,
            "deskripsi": deskripsi,
            "software": software,
            "deadline": deadline,
            "klien": klien,
            "status": status
        })
        print("\nProyek berhasil ditambahkan.")
    except ValueError as e:
        print(e)
    finally:
        pause()

def pilih_dan_update_proyek():
    clear_screen()
    print("=== UBAH PROYEK ===")
    from database.db_config import projects_table
    projects = projects_table.all()
    if projects:
        choices = [f"{i+1}. {p['judul']}" for i, p in enumerate(projects)]
        pilih = inquirer.prompt([inquirer.List("pilih", message="Pilih proyek", choices=choices)])
        index = int(pilih["pilih"].split(".")[0]) - 1
        update_proyek(index)
    else:
        print("Belum ada proyek.")
        pause()

def update_proyek(index):
    clear_screen()
    projects = projects_table.all()
    if not projects:
        print("Belum ada proyek.")
        pause()
        return
    
    clear_screen()
    while True:
        print(f"=== UBAH PROYEK: {projects[index]['judul']} ===")
        pertanyaan = [
            inquirer.List("pilih", message="Pilih data yang ingin diubah", choices=[
                "Judul", "Deskripsi", "Software", "Deadline", "Klien", "Status", "Selesai Update"
            ])
        ]
        jawaban = inquirer.prompt(pertanyaan)
        pilih = jawaban["pilih"]
        if pilih == "Selesai Update":
            break
        new_value = input(f"Masukkan {pilih.lower()} baru: ")
        projects_table.update({pilih.lower(): new_value}, doc_ids=[projects[index].doc_id])
        clear_screen()
    print("\nData proyek berhasil diperbarui.")
    pause()


def hapus_proyek():
    clear_screen()
    print("=== HAPUS PROYEK ===")
    projects = projects_table.all()
    if not projects:
        print("Belum ada proyek.")
        pause()
        return

    choices = [f"{i+1}. {p['judul']}" for i, p in enumerate(projects)]
    questions = [inquirer.List("pilih", message="Pilih proyek yang ingin dihapus", choices=choices)]
    jawaban = inquirer.prompt(questions)
    nomor = int(jawaban["pilih"].split(".")[0]) - 1

    konfirmasi = input(f"Hapus proyek '{projects[nomor]['judul']}'? (y/n): ").lower()
    if konfirmasi == "y":
        projects_table.remove(doc_ids=[projects[nomor].doc_id])
        print("Proyek berhasil dihapus.")
    else:
        print("Dibatalkan.")
    pause()
