import Head from 'next/head'
import Image from 'next/image'
import NormalLayout from 'components/layouts/NormalLayout'
import OrderHistory from 'components/OrderHistory/OrderHistory'

export default function OrderHistoryPage() {
    return (
        <OrderHistory />
    )
}


OrderHistoryPage.getLayout = function getLayout(page) {
    return (
        <NormalLayout>
            {page}
        </NormalLayout>
    )
}