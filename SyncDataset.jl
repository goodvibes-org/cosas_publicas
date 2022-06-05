using CSV, DataFrames, GoogleDrive

const SHEET_URL = "https://docs.google.com/spreadsheets/d/1fayGax49aN2YCLPYyb_MX2x5ZuIDQWanjo76BOu9sNs/edit?usp=sharing"
const FILE_PATH = join([@__DIR__, "/files"])



df = drive_download(SHEET_URL, FILE_PATH) |> CSV.File |> DataFrame



##### UNFINISHED ########