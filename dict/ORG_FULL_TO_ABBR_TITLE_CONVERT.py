import pickle
ORG_FULL_TO_ABBR_TITLE_CONVERT = {
    # investment
    # บงล.':'บริษัทเงินทุนหลักทรัพย์
    # บลจ.':'บริษัทหลักทรัพย์จัดการกองทุน
    # บง.':'บริษัทเงินทุน
    # บล.':'บริษัทหลักทรัพย์
    # bank
    'ธนาคาร': 'ธนาคาร',
    # branch
    'สาขา': 'สาขา',
    # General_First
    'การเคหะ': 'การเคหะ',
    'การไฟฟ้า': 'การไฟฟ้า',
    'การทาง': 'การทาง',
    'การท่องเที่ยว': 'การท่องเที่ยว',
    'การปิโตร': 'การปิโตร',
    'การประปา': 'การประปา',
    'การรถไฟ': 'การรถไฟ',
    'การนิคม': 'การนิคม',
    'กรม': 'กรม',
    'กระทรวง': 'กระทรวง',
    'กองกลาง': 'กองกลาง',
    'กองทุน': 'กองทุน',
    'กิจการ': 'กิจการ',
    'กิจกรรม': 'กิจกรรม',
    'แขวงการทาง': 'แขวงการทาง',
    'เครือข่าย': 'เครือข่าย',
    'โครงการ': 'โครงการ',
    'คณะบุคคล': 'คณะบุคคล',
    'เงินกองทุน': 'เงินกองทุน',
    'ชมรม': 'ชมรม',
    'ชุมนุม': 'ชุมนุม',
    'เทศบาล': 'เทศบาล',
    'ทบวง': 'ทบวง',
    'ที่ทำการ': 'ที่ทำการ',
    'โบสถ์': 'โบสถ์',
    'บรรษัท': 'บรรษัท',
    'แผนก': 'แผนก',
    'ฝ่าย': 'ฝ่าย',
    'พรรค': 'พรรค',
    'พิพิธภัณ': 'พิพิธภัณ',
    'ฟาร์ม': 'ฟาร์ม',
    'ภาควิชา': 'ภาควิชา',
    'นิติบุคคล': 'นิติบุคคล',
    'มหาวิทยาลัย': 'มหาวิทยาลัย',
    'มัสยิด': 'มัสยิด',
    'มูลนิธิ': 'มูลนิธิ',
    'เรือนจำ': 'เรือนจำ',
    'โรงงาน': 'โรงงาน',
    'ร.ง.': 'โรงงาน',
    'โรงพยาบาล': 'โรงพยาบาล',
    'ร.พ.': 'โรงพยาบาล',
    'รพ.': 'โรงพยาบาล',
    'โรงเรียน': 'โรงเรียน',
    'ร.ร.': 'ร.ร.',
    'รร.': 'ร.ร.',
    'โรงแรม': 'โรงแรม',
    'ร้าน': 'ร้าน',
    'วัด': 'วัด',
    'วิทยาลัย': 'วิทยาลัย',
    'ศูนย์': 'ศูนย์',
    'สโมสร': 'สโมสร',
    'สถานี': 'สถานี',
    'สถาบัน': 'สถาบัน',
    'สน.ง.': 'สำนักงาน',
    'สนง.': 'สำนักงาน',
    'สภา': 'สภา',
    'สภต.': 'สภต.',
    'สภอ.': 'สภอ.',
    'สมาคม': 'สมาคม',
    'สหกรณ์การเกษตร': 'สหกรณ์การเกษตร',
    'สหกรณ์ออมทรัพย์': 'สหกรณ์ออมทรัพย์',
    'สหภาพ': 'สหภาพ',
    'สาธารณสุข': 'สาธารณสุข',
    'สายการบิน': 'สายการบิน',
    'สำนักงาน': 'สำนักงาน',
    'ส.น.ง.': 'สำนักงาน',
    'ส.นง.': 'สำนักงาน',
    'สุขาภิบาล': 'สุขาภิบาล',
    'เหล่ากาชาด': 'เหล่ากาชาด',
    'หอการค้า': 'หอการค้า',
    'องค์กร': 'องค์กร',
    'องค์การ': 'องค์การ',
    'อบต.': 'อบต.',
    'อบจ.': 'อบจ.',
    #
    'แขวง': 'แขวง',
    'คณะ': 'คณะ',
    'สำนัก': 'สำนัก',
    'สถาน': 'สถาน',
    'สหกรณ์': 'สหกรณ์',
    'องค์การ': 'องค์การ',
    'โรง': 'โรง',
    #
    'บริษัทเงินทุนหลักทรัพย์': 'บงล.',
    'บริษัทหลักทรัพย์จัดการกองทุน': 'บลจ.',
    'บริษัทเงินทุน': 'บง.',
    'บริษัทหลักทรัพย์': 'บล.',
    'บงล.': 'บงล.',
    'บลง.': 'บงล.',
    'บลจ.': 'บลจ.',
    'บจล.': 'บลจ.',
    'บงล': 'บงล.',
    'บลง': 'บงล.',
    'บลจ': 'บลจ.',
    'บจล': 'บลจ.',
    'บ.ง.ล.': 'บงล.',
    'บ.ล.ง.': 'บงล.',
    'บ.ล.จ.': 'บลจ.',
    'บ.จ.ล.': 'บลจ.',
    'บ.งล': 'บงล.',
    'บ.ลง': 'บงล.',
    'บ.ลจ': 'บลจ.',
    'บ.จล': 'บลจ.',
    'บง.ล': 'บงล.',
    'บล.ง': 'บงล.',
    'บล.จ': 'บลจ.',
    'บจ.ล': 'บลจ.',
    'บง.ล.': 'บงล.',
    'บล.ง.': 'บงล.',
    'บล.จ.': 'บลจ.',
    'บจ.ล.': 'บลจ.',
    'บ.งล.': 'บงล.',
    'บ.ลง.': 'บงล.',
    'บ.ลจ.': 'บลจ.',
    'บ.จล.': 'บลจ.',
    'บ.ง.ล': 'บงล.',
    'บ.ล.ง': 'บงล.',
    'บ.ล.จ': 'บลจ.',
    'บ.จ.ล': 'บลจ.',
    'บง.': 'บง.',
    'บล.': 'บล.',
    'บ.ง': 'บง.',
    'บ.ล': 'บล.',
    'บ.ง.': 'บง.',
    'บ.ล.': 'บล.',
    # ห้างหุ้นส่วน
    'ห้างหุ้นส่วนจำกัด': 'หจก.',
    'ห้างหุ้นส่วน': 'หจก.',
    'ห้างหุ้นส่วนสามัญนิติบุคคล': 'หสน.',
    'ห้างหุ้นส่วนสามัญ': 'หส.',
    'หส.': 'หส.',
    'ห.ส.': 'หส.',
    'ห.ส': 'หส.',
    'หส': 'หส.',
    'หสม.': 'หส.',
    'หจก.': 'หจก.',
    'หสน.': 'หสน.',
    'หกจ.': 'หจก.',
    'หนส.': 'หสน.',
    'หจก': 'หจก.',
    'หสน': 'หสน.',
    'หกจ': 'หจก.',
    'หนส': 'หสน.',
    'ห.จ.ก.': 'หจก.',
    'ห.ส.น.': 'หสน.',
    'ห.ก.จ.': 'หจก.',
    'ห.น.ส.': 'หสน.',
    'ห.จก': 'หจก.',
    'ห.สน': 'หสน.',
    'ห.กจ': 'หจก.',
    'ห.นส': 'หสน.',
    'หจ.ก': 'หจก.',
    'หส.น': 'หสน.',
    'หก.จ': 'หจก.',
    'หน.ส': 'หสน.',
    'หจ.ก.': 'หจก.',
    'หส.น.': 'หสน.',
    'หก.จ.': 'หจก.',
    'หน.ส.': 'หสน.',
    'ห.จก.': 'หจก.',
    'ห.สน.': 'หสน.',
    'ห.กจ.': 'หจก.',
    'ห.นส.': 'หสน.',
    'ห.จ.ก': 'หจก.',
    'ห.ส.น': 'หสน.',
    'ห.ก.จ': 'หจก.',
    'ห.น.ส': 'หสน.',
    # Correction
    #บจ. correction
    'บจก.': 'บจ.',
    'บกจ.': 'บจ.',
    'บจก': 'บจ.',
    'บกจ': 'บจ.',
    'บ.จ.ก.': 'บจ.',
    'บ.ก.จ.': 'บจ.',
    'บ.จก': 'บจ.',
    'บ.กจ': 'บจ.',
    'บจ.ก': 'บจ.',
    'บก.จ': 'บจ.',
    'บจ.ก.': 'บจ.',
    'บก.จ.': 'บจ.',
    'บ.จก.': 'บจ.',
    'บ.กจ.': 'บจ.',
    'บ.จ.ก': 'บจ.',
    'บ.ก.จ': 'บจ.',
    'บจ.': 'บจ.',
    'บจ': 'บจ.',
    'บ.จ': 'บจ.',
    'บ.จ.': 'บจ.',
    'บจง': 'บจ.',
    #บมจ. correction
    'บมจ.': 'บมจ.',
    'บจม.': 'บมจ.',
    'บมจ': 'บมจ.',
    'บจม': 'บมจ.',
    'บ.ม.จ.': 'บมจ.',
    'บ.จ.ม.': 'บมจ.',
    'บ.มจ': 'บมจ.',
    'บ.จม': 'บมจ.',
    'บม.จ': 'บมจ.',
    'บจ.ม': 'บมจ.',
    'บม.จ.': 'บมจ.',
    'บจ.ม.': 'บมจ.',
    'บ.มจ.': 'บมจ.',
    'บ.จม.': 'บมจ.',
    'บ.ม.จ': 'บมจ.',
    'บ.จ.ม': 'บมจ.',
    # correction
    'บริษัท': 'บจ.',
    '<ริษัท': 'บจ.',
    '<บริษัท': 'บจ.',
    '@ริษัท': 'บจ.',
    'บริษท': 'บจ.',
    'ยริษัท': 'บจ.',
    'บ.': 'บจ.',
    '[บริษัท': 'บจ.',
    'จำกัด': 'จำกัด',
    'จากัด': 'จำกัด',
    'จ.ก.': 'จำกัด',
    'จก.': 'จำกัด',
    'จำกัด': 'จำกัด',
    'จำกัด.': 'จำกัด',
    'จากัด': 'จำกัด',
    'จ.ก.': 'จำกัด',
    'จ.ก': 'จำกัด',
    'จก.': 'จำกัด',
    'กำกัด': 'จำกัด',
    'จำกัน': 'จำกัด',
    'จำกัอ': 'จำกัด',
    'จักัด': 'จำกัด',
    'มหาชน': 'มหาชน'
}

if __name__ == "__main__":
    with open('dict/ORG_FULL_TO_ABBR_TITLE_CONVERT.dictionary', 'wb') as dictionary_file:
        pickle.dump(ORG_FULL_TO_ABBR_TITLE_CONVERT, dictionary_file)