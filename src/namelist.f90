module namelist

    use globals, only : nx, ny, nz, &
                      & time_ini, year_num, records_day, number_of_variables=>vars, variable_number=>var_number, &
                      & input_file, output_file

    implicit none

    private
    public :: read_nml

    integer :: time_fin

    contains


    subroutine read_nml()
        
        namelist / grid / nx, ny, nz
        namelist / record / time_ini, time_fin, records_day, number_of_variables, variable_number
        namelist / files / input_file, output_file

        nx = 0
        ny = 0
        nz = 0

        time_ini            = 0
        time_fin            = 0
        records_day         = 0
        number_of_variables = 0
        variable_number     = 0

        input_file  = ''
        output_file = ''

        read(5,nml=grid  )
        read(5,nml=record)
        read(5,nml=files )
        
        call checker()

        year_num = (time_fin - time_ini+1) / (365*records_day)

        if (year_num*365*records_day /= time_fin-time_ini+1) then
            write(0,'(A)') 'ERROR STOP'
            write(0,'(A)') 'time_ini, time_fin, or records_day is invalid'
            write(0,'(A)') 'time_fin does not specify the last record of the climatological mean period'
            write(0,'(A)') 'Note that the input data must not include leap days'
            ERROR STOP
        endif

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

        if (time_ini <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid time_ini value : ', time_ini
            write(0,'(A)')    'time_ini must be more than 0'
            ERROR STOP
        endif

        if (time_fin <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid time_fin value : ', time_fin
            write(0,'(A)')    'time_fin must be more than 0'
            ERROR STOP
        endif

        if (records_day <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid records_day value : ', records_day
            write(0,'(A)')    'records_day must be more than 0'
            ERROR STOP
        endif

        if (number_of_variables <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid number_of_variables value : ', number_of_variables
            write(0,'(A)')    'number_of_variables must be more than 0'
            ERROR STOP
        endif

        if (variable_number <= 0) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A,I0)') 'Invalid variable_number value : ', variable_number
            write(0,'(A)')    'variable_number must be more than 0'
            ERROR STOP
        endif

        if (variable_number > number_of_variables) then
            write(0,'(A)')    'ERROR STOP'
            write(0,'(A)')    'variable_number or number_of_variables is invalid'
            write(0,'(A,I0)') 'number_of_variables : ', number_of_variables
            write(0,'(A,I0)') 'variable_number     : ', variable_number
            write(0,'(A)')    'variable_number must be equal or smaller than number_of_variables'
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

