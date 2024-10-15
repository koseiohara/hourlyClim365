module shifter

    use globals, only : kp, nx, ny, nz, yearend_record, final_record, output_initial_record, input_file, output_file
    use BinIO  , only : finfo, fopen, fclose, fread, fwrite, get_record, reset_record

    implicit none

    private
    public :: time_shift

    contains


    subroutine time_shift()
        type(finfo) :: ifile
        type(finfo) :: ofile

        real(kp) :: work_container(nx,ny,nz)
        integer  :: irec

        integer :: debug

        call fopen(ifile              , &  !! OUT
                 & file   =input_file , &  !! IN
                 & action ='READ'     , &  !! IN
                 & record =1          , &  !! IN
                 & recl   =kp*nx*ny*nz, &  !! IN
                 & recstep=1            )  !! IN

        call fopen(ofile                        , &  !! OUT
                 & file   =output_file          , &  !! IN
                 & action ='WRITE'              , &  !! IN
                 & record =output_initial_record, &  !! IN
                 & recl   =kp*nx*ny*nz          , &  !! IN
                 & recstep=1                      )  !! IN

        do irec = 1, yearend_record
            call get_record(ofile, debug)
            write(*,'(I0,"  >>  ",I0)') irec, debug

            call fread(ifile                         , &  !! INOUT
                     & work_container(1:nx,1:ny,1:nz)  )  !! OUT

            call fwrite(ofile                         , &  !! INOUT
                      & work_container(1:nx,1:ny,1:nz)  )  !! IN
        enddo

        call reset_record(ofile      , &  !! INOUT
                        & newrecord=1  )  !! IN

        do irec = yearend_record+1, final_record
            call get_record(ofile, debug)
            write(*,'(I0,"  >>  ",I0)') irec, debug

            call fread(ifile                         , &  !! INOUT
                     & work_container(1:nx,1:ny,1:nz)  )  !! OUT

            call fwrite(ofile                         , &  !! INOUT
                      & work_container(1:nx,1:ny,1:nz)  )  !! IN
        enddo

        call fclose(ifile)  !! INOUT
        call fclose(ofile)  !! INOUT

    end subroutine time_shift


end module shifter

