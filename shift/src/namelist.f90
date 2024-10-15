module namelist

    use globals, only : nx, ny, nz, &
                      & yearend_record, final_record, output_initial_record, &
                      & input_file, output_file

    implicit none

    private
    public :: read_nml


    contains


    subroutine read_nml()
        
        namelist / grid / nx, ny, nz
        namelist / record / yearend_record, final_record
        namelist / files / input_file, output_file

        nx = 0
        ny = 0
        nz = 0

        yearend_record = 0
        final_record   = 0

        input_file  = ''
        output_file = ''

        read(5,nml=grid  )
        read(5,nml=record)
        read(5,nml=files )
        
        call checker()

        output_initial_record = final_record - yearend_record + 1

    end subroutine read_nml


    subroutine checker()

        if (nx <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid nx value : ', nx
            write(0,'(A)')    'nx must be more than 0'
            ERROR STOP
        endif

        if (ny <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid ny value : ', ny
            write(0,'(A)')    'ny must be more than 0'
            ERROR STOP
        endif

        if (nz <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid nz value : ', nz
            write(0,'(A)')    'nz must be more than 0'
            ERROR STOP
        endif

        if (yearend_record <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid yearend_record value : ', yearend_record
            write(0,'(A)')    'yearend_record must be more than 0'
            ERROR STOP
        endif

        if (final_record <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid final_record value : ', final_record
            write(0,'(A)')    'final_record must be more than 0'
            ERROR STOP
        endif

        if (yearend_record >= final_record) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid yearend_record value : ', yearend_record
            write(0,'(A)')    'yearend_record must be less than final_record value'
            ERROR STOP
        endif

        if (trim(input_file) == '') then
            write(0,'(A)') 'ERROR STOP'
            write(0,'(A)') 'input_file is not specified'
            ERROR STOP
        endif

        if (trim(output_file) == '') then
            write(0,'(A)') 'ERROR STOP'
            write(0,'(A)') 'output_file is not specified'
            ERROR STOP
        endif

    end subroutine checker


end module namelist

