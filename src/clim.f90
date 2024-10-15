module clim

    use globals , only : kp, nx, ny, nz, time_ini, year_num, records_day, vars, var_number, input_file, output_file
    use BinIO   , only : finfo, fopen, fclose, fread, fwrite, get_record, reset_record
    use debugger, only : debug_open, debug_close, debug_write, debug_linebreak
    use interp  , only : interp_linear_y

    implicit none

    private
    public :: hourly_clim_365

    contains


    subroutine hourly_clim_365()
        type(finfo) :: ifile
        type(finfo) :: ofile
        real(kp) :: reader(nx,ny,nz)
        real(kp) :: mean(nx,ny,nz)

        integer :: initial_record
        integer :: year
        integer :: t

        call fopen(ifile                               , &  !! OUT
                 & file   =input_file                  , &  !! IN
                 & action ='READ'                      , &  !! IN
                 & record =vars*(time_ini-1)+var_number, &  !! IN
                 & recl   =kp*nx*ny*nz                 , &  !! IN
                 & recstep=0                             )  !! IN

        call fopen(ofile              , &  !! OUT
                 & file   =output_file, &  !! IN
                 & action ='WRITE'    , &  !! IN
                 & record =1          , &  !! IN
                 & recl   =kp*nx*ny*nz, &  !! IN
                 & recstep=1            )  !! IN

        call debug_open()

        do t = 1, 365*records_day
            mean(1:nx,1:ny,1:nz) = 0._kp
            
            call get_record(ifile         , &  !! IN
                          & initial_record  )  !! OUT

            do year = 1, year_num

                call debug_write(ifile)  !! IN

                call fread(ifile                 , &  !! INOUT
                         & reader(1:nx,1:ny,1:nz)  )  !! IN

                mean(1:nx,1:ny,1:nz) = mean(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)

                call reset_record(ifile                         , &  !! INOUT
                                & increment=365*records_day*vars  )  !! IN
            enddo

            mean(1:nx,1:ny,1:nz) = mean(1:nx,1:ny,1:nz) / real(year_num, kind=kp)

            call interp_linear_y(mean(1:nx,1:ny,1:nz))  !! INOUT

            call fwrite(ofile               , &  !! INOUT
                      & mean(1:nx,1:ny,1:nz)  )  !! IN

            call reset_record(ifile                        , &  !! INOUT
                            & newrecord=initial_record+vars  )  !! IN

            call debug_linebreak()
        enddo

        call fclose(ifile)  !! INOUT
        call fclose(ofile)  !! INOUT

        call debug_close()

    end subroutine hourly_clim_365


end module clim

