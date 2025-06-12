import SimpleITK as sitk
import os

class Config:
    DIR_IDS = ['3', '5', '6'] # specify your folder name here
    BASE_DICOM_DIR = "./images/dicom"
    NIFTI_DIR = "./images/nifti"
    RESULT = "./result"

def convert_dicom_to_nifti():
    os.makedirs(Config.NIFTI_DIR, exist_ok=True)
    os.makedirs(Config.RESULT, exist_ok=True)

    for dir_id in Config.DIR_IDS:
        dicom_dir = os.path.join(Config.BASE_DICOM_DIR, dir_id)

        if not os.path.isdir(dicom_dir):
            print(f"Directory not found: {dicom_dir}")
            continue

        series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(dicom_dir)
        if not series_IDs:
            raise RuntimeError(f"No DICOM series found in {dicom_dir}")

        series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(dicom_dir, series_IDs[0])

        reader = sitk.ImageSeriesReader()
        reader.SetFileNames(series_file_names)
        image3D = reader.Execute()

        output_path = os.path.join(Config.NIFTI_DIR, f"raw_{dir_id}.nii")
        sitk.WriteImage(image3D, output_path)

        print(f"Written: {output_path}")

if __name__ == "__main__":
    convert_dicom_to_nifti()