; Data Section
SECTION .DATA
    users:     DB "mihsanr81", "2509106081", "admin", 0  ; Initial user data
    projects:  TIMES 100 DB 0  ; Array for projects storage
    
; Program Start
START:
    CALL CLEAR_SCREEN
    CALL MAIN_MENU

; Main Menu
MAIN_MENU:
    PRINT "=== SISTEM MANAJEMEN PROYEK DESAIN GRAFIS ==="
    PRINT "1. Login"
    PRINT "2. Register" 
    PRINT "3. Keluar"
    INPUT menu_choice
    
    CMP menu_choice, "1"
    JE LOGIN_PROCESS
    CMP menu_choice, "2"
    JE REGISTER_PROCESS
    CMP menu_choice, "3"
    JE EXIT_PROGRAM
    JMP MAIN_MENU

; Login Process
LOGIN_PROCESS:
    CALL CLEAR_SCREEN
    PRINT "=== LOGIN ==="
    INPUT username
    INPUT password
    
    ; Search for user in users array
    MOV SI, users          ; Source index for users array
    MOV user_found, 0
    
SEARCH_USER_LOOP:
    CMP [SI], 0           ; Check if end of array
    JE USER_NOT_FOUND
    
    ; Compare username
    MOV DI, username
    CALL COMPARE_STRINGS
    CMP strings_equal, 1
    JNE NEXT_USER
    
    ; Compare password  
    MOV DI, password
    ADD SI, 1             ; Move to password field
    CALL COMPARE_STRINGS
    CMP strings_equal, 1
    JNE NEXT_USER
    
    ; User found and authenticated
    MOV user_found, 1
    MOV current_user, SI  ; Store pointer to user data
    JMP CHECK_USER_ROLE
    
NEXT_USER:
    ADD SI, 3             ; Move to next user (3 fields each)
    JMP SEARCH_USER_LOOP

USER_NOT_FOUND:
    PRINT "Login gagal! Username atau password salah."
    CALL PRESS_ENTER
    JMP MAIN_MENU

CHECK_USER_ROLE:
    MOV AX, [current_user]
    ADD AX, 2             ; Move to role field
    CMP [AX], "admin"
    JE ADMIN_MENU
    JMP USER_MENU

; Admin Menu
ADMIN_MENU:
ADMIN_LOOP:
    CALL CLEAR_SCREEN
    PRINT "=== MENU ADMIN ==="
    PRINT "1. Tambah Proyek"
    PRINT "2. Lihat Proyek"
    PRINT "3. Update Proyek" 
    PRINT "4. Hapus Proyek"
    PRINT "5. Logout"
    INPUT admin_choice
    
    CMP admin_choice, "1"
    JE ADD_PROJECT
    CMP admin_choice, "2"
    JE VIEW_PROJECTS
    CMP admin_choice, "3"
    JE UPDATE_PROJECT
    CMP admin_choice, "4"
    JE DELETE_PROJECT
    CMP admin_choice, "5"
    JE MAIN_MENU
    JMP ADMIN_LOOP

; Add Project (CREATE)
ADD_PROJECT:
    CALL CLEAR_SCREEN
    PRINT "=== TAMBAH PROYEK ==="
    INPUT project_title
    INPUT project_description
    INPUT project_software
    INPUT project_deadline
    INPUT project_client
    INPUT project_status
    
    ; Validate required fields
    CMP project_title, ""
    JE MISSING_FIELDS
    CMP project_client, ""
    JE MISSING_FIELDS
    
    ; Add project to projects array
    CALL ADD_TO_PROJECTS_ARRAY
    PRINT "Proyek berhasil ditambah!"
    JMP ADMIN_WAIT

MISSING_FIELDS:
    PRINT "Wajib diisi!"
    JMP ADMIN_WAIT

; View Projects (READ)
VIEW_PROJECTS:
    CALL CLEAR_SCREEN
    PRINT "=== DAFTAR PROYEK ==="
    
    MOV CX, projects_count
    CMP CX, 0
    JE NO_PROJECTS
    
    MOV SI, projects
DISPLAY_PROJECTS_LOOP:
    PRINT f"\n[{SI+1}] {[SI].title}"      ; Project title
    PRINT f"Deskripsi: {[SI].description}"
    PRINT f"Software : {[SI].software}"
    PRINT f"Deadline : {[SI].deadline}"
    PRINT f"Klien    : {[SI].client}"
    PRINT f"Status   : {[SI].status}"
    
    ADD SI, 6              ; Move to next project (6 fields each)
    LOOP DISPLAY_PROJECTS_LOOP
    JMP ADMIN_WAIT

NO_PROJECTS:
    PRINT "Belum ada proyek."
    JMP ADMIN_WAIT

; Update Project
UPDATE_PROJECT:
    CALL CLEAR_SCREEN
    PRINT "=== UBAH PROYEK ==="
    
    CMP projects_count, 0
    JE NO_PROJECTS_UPDATE
    
    ; Display project list
    MOV SI, projects
    MOV CX, projects_count
DISPLAY_FOR_UPDATE:
    PRINT f"[{CX}] {[SI].title}"
    ADD SI, 6
    LOOP DISPLAY_FOR_UPDATE
    
    INPUT project_number
    CALL VALIDATE_NUMBER
    CMP number_valid, 0
    JE INVALID_NUMBER_UPDATE
    
    ; Convert to zero-based index
    SUB project_number, 1
    CALL GET_PROJECT_POINTER
    CMP project_ptr, 0
    JE INVALID_PROJECT
    
UPDATE_MENU:
    CALL CLEAR_SCREEN
    PRINT f"=== UBAH PROYEK: {[project_ptr].title} ==="
    PRINT "1. Judul"
    PRINT "2. Deskripsi"
    PRINT "3. Software"
    PRINT "4. Deadline"
    PRINT "5. Klien"
    PRINT "6. Status"
    PRINT "7. Selesai Update"
    INPUT update_choice
    
    CMP update_choice, "1"
    JE UPDATE_TITLE
    CMP update_choice, "2"
    JE UPDATE_DESCRIPTION
    CMP update_choice, "3"
    JE UPDATE_SOFTWARE
    CMP update_choice, "4"
    JE UPDATE_DEADLINE
    CMP update_choice, "5"
    JE UPDATE_CLIENT
    CMP update_choice, "6"
    JE UPDATE_STATUS
    CMP update_choice, "7"
    JE UPDATE_COMPLETE
    JMP UPDATE_MENU

UPDATE_TITLE:
    INPUT new_title
    MOV [project_ptr].title, new_title
    JMP UPDATE_MENU

UPDATE_DESCRIPTION:
    INPUT new_description
    MOV [project_ptr].description, new_description
    JMP UPDATE_MENU

UPDATE_SOFTWARE:
    INPUT new_software
    MOV [project_ptr].software, new_software
    JMP UPDATE_MENU

UPDATE_DEADLINE:
    INPUT new_deadline
    MOV [project_ptr].deadline, new_deadline
    JMP UPDATE_MENU

UPDATE_CLIENT:
    INPUT new_client
    MOV [project_ptr].client, new_client
    JMP UPDATE_MENU

UPDATE_STATUS:
    INPUT new_status
    MOV [project_ptr].status, new_status
    JMP UPDATE_MENU

UPDATE_COMPLETE:
    PRINT "Data proyek berhasil diperbarui!"
    JMP ADMIN_WAIT

NO_PROJECTS_UPDATE:
    PRINT "Belum ada proyek."
    JMP ADMIN_WAIT

INVALID_NUMBER_UPDATE:
    PRINT "Input harus angka."
    JMP ADMIN_WAIT

INVALID_PROJECT:
    PRINT "Nomor proyek tidak valid."
    JMP ADMIN_WAIT

; Delete Project
DELETE_PROJECT:
    CALL CLEAR_SCREEN
    PRINT "=== HAPUS PROYEK ==="
    
    CMP projects_count, 0
    JE NO_PROJECTS_DELETE
    
    ; Display project list
    MOV SI, projects
    MOV CX, projects_count
DISPLAY_FOR_DELETE:
    PRINT f"[{CX}] {[SI].title}"
    ADD SI, 6
    LOOP DISPLAY_FOR_DELETE
    
    INPUT delete_number
    CALL VALIDATE_NUMBER
    CMP number_valid, 0
    JE INVALID_NUMBER_DELETE
    
    ; Convert to zero-based index
    SUB delete_number, 1
    CALL GET_PROJECT_POINTER
    CMP project_ptr, 0
    JE INVALID_PROJECT_DELETE
    
    PRINT f"Hapus proyek '{[project_ptr].title}'? (y/n): "
    INPUT confirmation
    
    CMP confirmation, "y"
    JE CONFIRM_DELETE
    CMP confirmation, "Y"
    JE CONFIRM_DELETE
    
    PRINT "Dibatalkan."
    JMP ADMIN_WAIT

CONFIRM_DELETE:
    CALL REMOVE_FROM_PROJECTS_ARRAY
    PRINT "Proyek dihapus!"
    JMP ADMIN_WAIT

NO_PROJECTS_DELETE:
    PRINT "Belum ada proyek."
    JMP ADMIN_WAIT

INVALID_NUMBER_DELETE:
    PRINT "Input harus angka."
    JMP ADMIN_WAIT

INVALID_PROJECT_DELETE:
    PRINT "Nomor tidak valid."
    JMP ADMIN_WAIT

ADMIN_WAIT:
    CALL PRESS_ENTER
    JMP ADMIN_LOOP

; User Menu
USER_MENU:
USER_LOOP:
    CALL CLEAR_SCREEN
    PRINT f"=== MENU PENGGUNA ({[current_user].username}) ==="
    PRINT "1. Lihat Proyek"
    PRINT "2. Logout"
    INPUT user_choice
    
    CMP user_choice, "1"
    JE USER_VIEW_PROJECTS
    CMP user_choice, "2"
    JE MAIN_MENU
    JMP USER_LOOP

USER_VIEW_PROJECTS:
    CALL CLEAR_SCREEN
    PRINT "=== DAFTAR PROYEK ==="
    
    MOV CX, projects_count
    CMP CX, 0
    JE USER_NO_PROJECTS
    
    MOV SI, projects
USER_DISPLAY_LOOP:
    PRINT f"\n[{SI+1}] {[SI].title}"
    PRINT f"Deskripsi: {[SI].description}"
    PRINT f"Software : {[SI].software}"
    PRINT f"Deadline : {[SI].deadline}"
    PRINT f"Klien    : {[SI].client}"
    PRINT f"Status   : {[SI].status}"
    
    ADD SI, 6
    LOOP USER_DISPLAY_LOOP
    JMP USER_WAIT

USER_NO_PROJECTS:
    PRINT "Belum ada proyek."
    JMP USER_WAIT

USER_WAIT:
    CALL PRESS_ENTER
    JMP USER_LOOP

; Registration Process
REGISTER_PROCESS:
    CALL CLEAR_SCREEN
    PRINT "=== REGISTER ==="
    INPUT new_username
    INPUT new_password
    
    ; Check if username exists
    MOV SI, users
CHECK_USERNAME_LOOP:
    CMP [SI], 0
    JE USERNAME_AVAILABLE
    
    MOV DI, new_username
    CALL COMPARE_STRINGS
    CMP strings_equal, 1
    JE USERNAME_EXISTS
    
    ADD SI, 3
    JMP CHECK_USERNAME_LOOP

USERNAME_AVAILABLE:
    ; Validate input
    CMP new_username, ""
    JE MISSING_REGISTER_FIELDS
    CMP new_password, ""
    JE MISSING_REGISTER_FIELDS
    
    ; Add new user
    CALL ADD_TO_USERS_ARRAY
    PRINT "Akun berhasil dibuat!"
    JMP REGISTER_WAIT

USERNAME_EXISTS:
    PRINT "Username sudah digunakan!"
    JMP REGISTER_WAIT

MISSING_REGISTER_FIELDS:
    PRINT "Username dan password wajib diisi!"
    JMP REGISTER_WAIT

REGISTER_WAIT:
    CALL PRESS_ENTER
    JMP MAIN_MENU

; Exit Program
EXIT_PROGRAM:
    CALL CLEAR_SCREEN
    PRINT "Terima kasih telah menggunakan program ini."
    HALT

; Utility Functions
CLEAR_SCREEN:
    ; OS-specific screen clearing implementation
    RET

PRESS_ENTER:
    PRINT "Tekan Enter Untuk Melanjutkan..."
    WAIT_FOR_ENTER
    RET

COMPARE_STRINGS:
    ; Implementation for string comparison
    ; Sets strings_equal flag
    RET

VALIDATE_NUMBER:
    ; Implementation for number validation
    ; Sets number_valid flag
    RET

GET_PROJECT_POINTER:
    ; Calculate pointer to project at given index
    ; Sets project_ptr
    RET

ADD_TO_PROJECTS_ARRAY:
    ; Add new project to projects array
    ; Increments projects_count
    RET

REMOVE_FROM_PROJECTS_ARRAY:
    ; Remove project from projects array
    ; Decrements projects_count
    RET

ADD_TO_USERS_ARRAY:
    ; Add new user to users array
    RET